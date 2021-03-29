#!/usr/bin/env python

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.storage import StorageManagementClient
from relay_sdk import Interface, Dynamic as D

relay = Interface()

credentials = ServicePrincipalCredentials(
    client_id=relay.get(D.azure.connection.clientID),
    secret=relay.get(D.azure.connection.secret),
    tenant=relay.get(D.azure.connection.tenantID)
)
subscription_id=relay.get(D.azure.connection.subscriptionID)
storage_client = StorageManagementClient(credentials, subscription_id)

list_of_accounts = []
raw_accounts=None

# If resource group is specified, use that
rg = ''
try:
  rg=relay.get(D.resourceGroup)
except:
  print('No resource group specified. Looking up all Storage Accounts under subscription id.')

if (rg):
  print('Looking up all Storage Accounts under resource group {0}'.format(rg))
  raw_accounts = storage_client.storage_accounts.list_by_resource_group(rg)

else: 
  raw_accounts = storage_client.storage_accounts.list()

print('\nFound the following Azure Storage Accounts:')
print("\n{:<100} {:<30} {:<30} {:<30}".format('NAME', 'LOCATION', 'STATE', 'TAGS')) 

for account in raw_accounts:
  print("{:<100} {:<30} {:<30} {:<30}".format(account.name, account.location, account.provisioning_state, str(account.tags)))
  list_of_accounts.append(account.as_dict())

print('\nSetting output `storageAccounts` to list of {0} found storage accounts'.format(len(list_of_accounts)))
relay.outputs.set('storageAccounts', list_of_accounts)
