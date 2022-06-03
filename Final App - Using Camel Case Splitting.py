import re
import nltk
from nltk.corpus import words
from itertools import chain
from nltk.corpus import stopwords
import pandas as pd
## Case 1 : Splitting the words in the Dataframe and checking with the Global Dicitionary

## Defining the Dictionary
words_list = words.words()
# print(len(words_list))
stop_words = list(stopwords.words('english'))
# print(len(words_list))
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabets:
	try:
		words_list.remove(i)
	except:
		pass
# print(len(words_list))
for i in stop_words:
	try:
		words_list.remove(i)
	except ValueError:
		pass
# print(len(words_list))

# print(len(words_list))
for i in words_list:
	if(len(i) == 2 or len(i) == 3 or len(i) == 4):
		try:
			words_list.remove(i)
		except ValueError:
			pass

def string_splitting(s):
	train_data = []
	x = re.findall("[/][|]",s)
	if x:
		train_data.append(s.split("/"))
	else:
		## Camel Case spliiting
		camel_Case_split = re.findall(r'[a-zA-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))',s)
		train_data.append(camel_Case_split)
	return train_data

df = pd.read_csv("AWSDataset.csv")
strings_to_split =['src/test/kotlin/com/dbs/bazr/backend/controllers/acls/DealAttributesSanitizerTest.kt',
	'src/main/kotlin/com/dbs/bazr/backend/controllers/MockController.kt',	'src/test/kotlin/com/dbs/bazr/backend/controllers/acls/DealAttributesSanitizerTest.kt',	'src/main/kotlin/com/dbs/bazr/backend/controllers/MockController.kt',	'8443/nexus/content/repositories/releases',	'/opt/rcn/reportx/omr/rdg/backups/reportx',	'8443/nexus/content/repositories/releases',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'4ecc2f9302b46666f69fc94f7db464b0c9f568ad',	'/IBNG/gr/api/payments/applications/d2pay',	'/ogw/load/services/IWSGService1/channels',	'8443/nexus/content/repositories/releases',	'getMatchingValueFromPredefinedColumnList',	'8443/nexus/content/repositories/releases',	'/opt/rcn/reportx/omr/rdg/backups/reportx',	'8443/nexus/content/repositories/releases',	'8443/dcifgit/users/nikhilbhandari/avatar',	'/opt/rcn/reportx/omr/rdg/backups/reportx',	'8443/dcifgit/users/nikhilbhandari/avatar',	'getMatchingValueFromPredefinedColumnList',	'8443/dcifgit/users/foongchunfoong/avatar',	'8443/nexus/content/repositories/releases',	'/rest/deleteTreeRecord/requestDetailsId/',	'8443/nexus/content/repositories/releases',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'8443/nexus/content/repositories/releases',	'8443/nexus/content/repositories/releases',	'url=filebrowser/ipc/api/v1/download/file',	'8443/nexus/content/repositories/releases',	'8443/nexus/content/repositories/releases',	'/IBNG/gr/api/payments/applications/d2pay',	'/ogw/load/services/IWSGService1/channels',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'com/loginSubscriberv2/logout/idealLogout',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'/Clients/Client360/Accounts/Loan/Details',	'com/loginSubscriberv2/logout/idealLogout',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',	'com/loginSubscriberv2/logout/idealLogout',	'2FaByFznkGIg2PbiFELDT2g4D3VU8Cz0sMCZ6iLW',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',
    	'2BH8HYIz1JbEl6tox4IT4TnY2fGdlwH7MxUY7d43',	'8506521BFC350652163895D4C26DEE124209AA9E',	'/Clients/Client360/Accounts/Loan/Details',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'/Clients/Client360/Accounts/Loan/Details',	'cmFmQWdlbnRVc2VyOnBENG9uM1VAMjAyMUFnI250',	'cmFmQWdlbnRVc2VyOnBENG9uM1VAMjAyMUFnI250',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'/Clients/Client360/Accounts/Loan/Details',	'/rest/deleteTreeRecord/requestDetailsId/',	'/Clients/Client360/Accounts/Loan/Details',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'Lnet/sf/jasperreports/engine/JRSortField',	'75c5e90a222ab406e416cbf590a5397028a52de3',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',	'com/v2/customers/productservices/enquiry',	'2BH8HYIz1JbEl6tox4IT4TnY2fGdlwH7MxUY7d43',	'simm/mrsg/oauth2/authorization/forgerock',	'2BH8HYIz1JbEl6tox4IT4TnY2fGdlwH7MxUY7d43',	'user/assemble/backup/assemble/metricbeat',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'2BH8HYIz1JbEl6tox4IT4TnY2fGdlwH7MxUY7d43',	'/rest/deleteTreeRecord/requestDetailsId/',	'com/v2/customers/productservices/enquiry',	'user/assemble/backup/assemble/metricbeat',	'8443/dcifgit/users/manikandarajan/avatar',	'2BH8HYIz1JbEl6tox4IT4TnY2fGdlwH7MxUY7d43',	'8443/dcifgit/users/manikandarajan/avatar',	'user/assemble/backup/assemble/metricbeat',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'limitCombinationIdsToDisableBankLimits=4',	'com/v2/customers/productservices/enquiry',	'service/v3/onboarding/autoScaling/enable',	'/Clients/Client360/Accounts/Loan/Details',	'/Clients/Client360/Accounts/Loan/Details',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'com/v2/customers/productservices/enquiry',	'user/assemble/backup/assemble/metricbeat',	'com/v2/customers/productservices/enquiry',	'user/assemble/backup/assemble/metricbeat',	'user/assemble/backup/assemble/metricbeat',	'user/assemble/backup/assemble/metricbeat',	'retrieveBioReferencesByListOfProspectIds',	'/IBNG/gr/api/payments/applications/d2pay',	'/ogw/load/services/IWSGService1/channels',	'pararun=/OthersReleases/iWork/Automation',	'InvoiceManagementApprovalFilterComponent',	'syncLimitChangeWithCountryLimitStructure',	'InvoiceManagementApprovalFilterComponent',	'server/announcement/save/exchange/portal',	'calculator/api/doa/realignment/calculate',	'server/announcement/save/exchange/portal',	'server/announcement/save/exchange/portal',	'f47393e440840097b55fe1699014749baaac4901',	'server/announcement/save/exchange/portal',	'f47393e440840097b55fe1699014749baaac4901',	'countByCounterpartyInAndCreatedOnBetween',	'countByCounterpartyInAndCreatedOnBetween',	'InvoiceManagementApprovalFilterComponent',	'service/configdependency/dependent/view/',	'InvoiceManagementApprovalFilterComponent',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'service/api/v1/email/online/templates/in',	'com/v1/customers/productservices/enquiry',	'com/v1/customers/productservices/enquiry',	'TermDepositTerminationCommandHandlerTest',	'InvoiceManagementApprovalFilterComponent',	'InvoiceManagementApprovalFilterComponent',	'TermDepositTerminationCommandHandlerTest',	'service/configdependency/dependent/view/',	'syncLimitChangeWithCountryLimitStructure',	'pararun=/OthersReleases/iWork/Automation',	'findBucketRiskFactorGroupsByRiskFactorId',	'packages/common/auth/context/authContext',	'pararun=/OthersReleases/iWork/Automation',	'getProductCategoryAuditHistoryByKeyValue',	'service/configdependency/dependent/view/',	'service/configdependency/dependent/view/',	'accountPlanKeyOpportunityDetailsFormPage',	'findBucketRiskFactorGroupsByRiskFactorId',	'pararun=/OthersReleases/iWork/Automation',	'packages/common/auth/context/authContext',	'convertCampaignToInstallmentCampaignBean',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'f47393e440840097b55fe1699014749baaac4901',	'convertCampaignToInstallmentCampaignBean',	'/query/digitalAdvisory/productCategories',	'accountPlanKeyOpportunityDetailsFormPage',	'pararun=/OthersReleases/iWork/Automation',	'accountPlanKeyOpportunityDetailsFormPage',	'/data/actions/ClientListing/associatedrm',	'accountPlanKeyOpportunityDetailsFormPage',	'/query/digitalAdvisory/productCategories',	'accountPlanKeyOpportunityDetailsFormPage',	'authenticator/src/main/resources/tableau',	'/query/digitalAdvisory/productCategories',	'getProductCategoryAuditHistoryByKeyValue',	'getProductCategoryAuditHistoryByKeyValue',	'/svaas/svgengine/saveCommonCustomization',	'InvoiceManagementApprovalFilterComponent',	'/common/taskcomplete/TaskCompleteApprove',	'authenticator/src/main/resources/tableau',	'findByIdChannelIdAndSpokeCifAndAnchorCif',	'/common/taskcomplete/TaskCompleteApprove',	'InvoiceManagementApprovalFilterComponent',	'InvoiceManagementApprovalFilterComponent',	'testShouldMapToPurposeOfTransferResponse',	'accountHoldingInquiryTechnicalError=MDCM',	'accessTokenGenerationPath=/iam/v1/access',	'MerchantPaymentPreparationServiceAdapter',	'getDefaultCrossBorderPaymentOrderOutcome',	'getEnableKongToValidateMMKAyaBankAccount',	'getEnableKongToValidateMMKAyaBankAccount',	'8506521BFC350652163895D4C26DEE124209AA9E',	'stockActivityTypes==OetStockMfeConstants',	'BalanceTransferApplicationStatusActivity',	'getAadharDetailsCountByShareHolderInfoId',	'getAadharDetailsCountByShareHolderInfoId',	'InvoiceManagementApprovalFilterComponent',	'InvoiceManagementApprovalFilterComponent',	'getAadharDetailsCountByShareHolderInfoId',	'getAadharDetailsCountByShareHolderInfoId',	'banking/customer/queryFixedDepositDetail',	'banking/customer/queryFixedDepositDetail',	'getAadharDetailsCountByShareHolderInfoId',	'getAadharDetailsCountByShareHolderInfoId',	'InvoiceManagementApprovalFilterComponent',	'/common/taskcomplete/TaskCompleteApprove',	'InvoiceManagementApprovalFilterComponent',	'findByIdChannelIdAndSpokeCifAndAnchorCif',	'relationshipGroupingClientCodeValueCheck',	'/query/digitalAdvisory/productCategories',	'/common/taskcomplete/TaskCompleteApprove',	'convertCampaignToInstallmentCampaignBean',	'convertCampaignToInstallmentCampaignBean',	'js/plugins/datatables/buttons/dataTables',	'js/plugins/datatables/buttons/dataTables',	'/query/digitalAdvisory/productCategories',	'convertCampaignToInstallmentCampaignBean',	'/home/currentyeardashboard/teamdashboard',	'TermDepositTerminationCommandHandlerTest',	'findByIdChannelIdAndSpokeCifAndAnchorCif',	'TermDepositTerminationCommandHandlerTest',	'convertCampaignToInstallmentCampaignBean',	'countByCounterpartyInAndCreatedOnBetween',	'/query/digitalAdvisory/productCategories',	'convertCampaignToInstallmentCampaignBean',	'getEnableKongToValidateMMKAyaBankAccount',	'BalanceTransferApplicationStatusActivity',	'getEnableKongToValidateMMKAyaBankAccount',	'prepareMaintenanceAlertWindowTransaction',	'8506521BFC350652163895D4C26DEE124209AA9E',	'alteredPartDF=addColumnsNotPresentInPart',	'/query/digitalAdvisory/productCategories',	'alteredPartDF=addColumnsNotPresentInPart',	'getEnableKongToValidateMMKAyaBankAccount',	'BalanceTransferApplicationStatusActivity',
        	'getEnableKongToValidateMMKAyaBankAccount',	'prepareMaintenanceAlertWindowTransaction',	'8506521BFC350652163895D4C26DEE124209AA9E',	'testShouldMapToPurposeOfTransferResponse',	'accountHoldingInquiryTechnicalError=MDCM',	'accessTokenGenerationPath=/iam/v1/access',	'MerchantPaymentPreparationServiceAdapter',	'getDefaultCrossBorderPaymentOrderOutcome',	'/query/digitalAdvisory/productCategories',	'com/dbs/c2e/mstd/cn/casa/api/repository/',	'countByCounterpartyInAndCreatedOnBetween',	'alteredPartDF=addColumnsNotPresentInPart',	'com/dbs/c2e/mstd/cn/casa/api/repository/',	'findByIdChannelIdAndSpokeCifAndAnchorCif',	'findByIdChannelIdAndSpokeCifAndAnchorCif',	'com/dbs/c2e/mstd/cn/casa/api/repository/',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'/data/actions/ClientListing/associatedrm',	'alteredPartDF=addColumnsNotPresentInPart',	'authenticator/src/main/resources/tableau',	'com/dbs/c2e/mstd/cn/casa/api/repository/',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'alteredPartDF=addColumnsNotPresentInPart',	'alteredPartDF=addColumnsNotPresentInPart',	'HOME=/Users/dbsmownerdp/Library/Android3',	'/sg/cbgba/databackup/onshore/uno/dataset',	'/sg/cbgba/databackup/onshore/uno/dataset',	'/sg/cbgba/databackup/onshore/uno/dataset',	'TermDepositTerminationCommandHandlerTest',	'f47393e440840097b55fe1699014749baaac4901',	'alteredPartDF=addColumnsNotPresentInPart',	'MadameMarketingPreferencesUpdateResponse',	'f47393e440840097b55fe1699014749baaac4901',	'f47393e440840097b55fe1699014749baaac4901',	'TermDepositTerminationCommandHandlerTest',	'HOME=/Users/dbsmownerdp/Library/Android3',	'alteredPartDF=addColumnsNotPresentInPart',	'TermDepositTerminationCommandHandlerTest',	'authenticator/src/main/resources/tableau',	'shouldCreateCustomerResourceFromSnapshot',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'shouldCreateCustomerResourceFromSnapshot',	'/svaas/svgengine/saveCommonCustomization',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'convertCampaignToInstallmentCampaignBean',	'alteredPartDF=addColumnsNotPresentInPart',	'/svaas/svgengine/saveCommonCustomization',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'convertCampaignToInstallmentCampaignBean',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'/components/bmapMaintence/uploadDownload',	'convertCampaignToInstallmentCampaignBean',	'/irec/prod/source/SG/murex/mxbondstatic/',	'alteredPartDF=addColumnsNotPresentInPart',	'/data/actions/ClientListing/associatedrm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'customer/template/CustomerOnboardingForm',	'advSearchWithAccountNumberMultipleResult',	'shouldConvertPreNormaliseContextToString',	'shouldConvertPreNormaliseContextToString',	'shouldConvertPreNormaliseContextToString',	'shouldConvertPreNormaliseContextToString',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'Codedisp34string1234string1234string1234',	'shouldCreateCustomerResourceFromSnapshot',	'app/views/configuration/yieldcurve/yield',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'trustStore=/cdat/keystore/jbossforDeploy',	'shouldConvertPreNormaliseContextToString',	'getRejectedRegistryTransferInInformation',	'getRejectedRegistryTransferInInformation',	'InvoicePaymentSettlementDetailsComponent',	'requestResponseLoggingInterceptorEnabled',	'/Position/WarningVaultClosePositionPopUp',	'shouldCreateCustomerResourceFromSnapshot',	'getRejectedRegistryTransferInInformation',	'getRejectedRegistryTransferInInformation',	'InvoicePaymentSettlementDetailsComponent',	'testShouldMapToPurposeOfTransferResponse',	'accountHoldingInquiryTechnicalError=MDCM',	'accessTokenGenerationPath=/iam/v1/access',	'MerchantPaymentPreparationServiceAdapter',	'getDefaultCrossBorderPaymentOrderOutcome',	'testMapBioReferenceResourceAfterCreation',	'trustStore=/cdat/keystore/jbossforDeploy',	'updateWalletReconWithAccCreateFailStatus',	'shouldCreateCustomerResourceFromSnapshot',	'shouldConvertPreNormaliseContextToString',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'requestWithoutBodyShouldReturnBadRequest',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'trustStore=/cdat/keystore/jbossforDeploy',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'shouldCreateCustomerResourceFromSnapshot',	'shouldConvertPreNormaliseContextToString',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldConvertPreNormaliseContextToString',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'shouldCreateCustomerResourceFromSnapshot',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'fAhjvQhBsSgUF3jqehmEYeHcPBWcNRYWdD76jgC3',	'f47393e440840097b55fe1699014749baaac4901',	'updateWalletReconWithAccCreateFailStatus',	'trustStore=/cdat/keystore/jbossforDeploy',	'updateWalletReconWithAccCreateFailStatus',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByCustomerIdentityNumberAndCinSuffix',	'findDistinctTableNoAndHackathonByCountry',	'findByOneBankIdAndLoginEmailAndHackathon',	'findByOneBankIdAndLoginEmailAndHackathon',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'accountPlanKeyOpportunityDetailsFormPage',	'DBSAccountPlanDetailsEditDraftPageModule',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'/vaultManagement/openVaultDiscrepancyPdf',	'findByCustomerIdentityNumberAndCinSuffix',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'core/source/devtools/kafka/kafkaproducer',	'/aws/api/pcloud/getDetails/ACCOUNTREVIEW',	'accountPlanKeyOpportunityDetailsFormPage',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'/aws/api/pcloud/getDetails/ACCOUNTREVIEW',	'banking/customer/queryFixedDepositDetail',	'banking/customer/queryFixedDepositDetail',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'/vaultManagement/openVaultDiscrepancyPdf',	'/vaultManagement/openVaultDiscrepancyPdf',	'/Position/WarningVaultClosePositionPopUp',	'banking/customer/queryFixedDepositDetail',	'banking/customer/queryFixedDepositDetail',	'rfdDetailScreenShouldBeDisplayedProperly',	'/Position/WarningVaultClosePositionPopUp',	'getProductCategoryAuditHistoryByKeyValue',	'getProductCategoryAuditHistoryByKeyValue',	'CustomerProfileSearchByPropertyFilterDTO',	'CustomerProfileSearchByPropertyFilterDTO',	'CustomerProfileSearchByPropertyFilterDTO',	'/aws/api/pcloud/getDetails/ACCOUNTREVIEW',	'sendMessageRequestInterruptWithVariables',	'/data/actions/workflow/getOverridingType',	'/aws/api/pcloud/getDetails/ACCOUNTREVIEW',	'sendMessageRequestInterruptWithVariables',	'/data/actions/workflow/getOverridingType',	'livePendingSettlementSubscriptionsStatus',	'livePendingSettlementSubscriptionsStatus',	'livePendingSettlementSubscriptionsStatus',	'livePendingSettlementSubscriptionsStatus',	'livePendingSettlementSubscriptionsStatus',	'/components/examples/InternalServerError',	'/components/examples/InternalServerError',	'/services/OverridingManagement/interface',	'/services/OverridingManagement/interface',	'/services/OverridingManagement/interface',
            	'/services/OverridingManagement/interface',	'capiMyInfoService/prepareApplicationForm',	'capiMyInfoService/prepareApplicationForm',	'UnRegisterSuccessVChkiddeRegisterDBSBank',	'UnRegisterSuccessVChkiddeRegisterDBSBank',	'UnRegisterSuccessVChkiddeRegisterDBSBank',	'UnRegisterSuccessVChkiddeRegisterDBSBank',	'testShouldGetResponseHeadersSuccessfully',	'testShouldThrowExceptionForPaidContracts',	'testShouldGetResponseHeadersSuccessfully',	'testShouldThrowExceptionForPaidContracts',	'hfmentityccySchema=getHFMEntityccySchema',	'hfmentityccySchema=getHFMEntityccySchema',	'hfmentityccySchema=getHFMEntityccySchema',	'testShouldGetResponseHeadersSuccessfully',	'testShouldThrowExceptionForPaidContracts',	'ProfileVerificationRequestConstraintTest',	'requestWithoutBodyShouldReturnBadRequest',	'ProfileVerificationRequestConstraintTest',	'countByCounterpartyInAndCreatedOnBetween',	'countByCounterpartyInAndCreatedOnBetween',	'rfdDetailScreenShouldBeDisplayedProperly',	'rfdDetailScreenShouldBeDisplayedProperly',	'getEnableKongToValidateMMKAyaBankAccount',	'BalanceTransferApplicationStatusActivity',	'getEnableKongToValidateMMKAyaBankAccount',	'8506521BFC350652163895D4C26DEE124209AA9E',	'getEnableKongToValidateMMKAyaBankAccount',	'BalanceTransferApplicationStatusActivity',	'getEnableKongToValidateMMKAyaBankAccount',	'8506521BFC350652163895D4C26DEE124209AA9E',	'getEnableKongToValidateMMKAyaBankAccount',	'BalanceTransferApplicationStatusActivity',	'getEnableKongToValidateMMKAyaBankAccount',	'8506521BFC350652163895D4C26DEE124209AA9E',	'populateHKTranslatePasswordWSResponseDTO',	'mockMadameDocumentDetailResponseFinCheck',	'findStaffPoolDataBySelectedPlatformIndex',	'findStaffPoolDataBySelectedPlatformIndex',	'AX6kxbPkJomBqAAC8xOqbihizskGJfqiqJjTVQ03',	'populateHKTranslatePasswordWSResponseDTO',	'findStaffPoolDataBySelectedPlatformIndex',	'findStaffPoolDataBySelectedPlatformIndex',	'AX6kxbPkJomBqAAC8xOqbihizskGJfqiqJjTVQ03',	'populateHKTranslatePasswordWSResponseDTO',	'populateHKTranslatePasswordWSResponseDTO',	'populateHKTranslatePasswordWSResponseDTO',	'populateHKTranslatePasswordWSResponseDTO',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'populateHKTranslatePasswordWSResponseDTO',	'populateHKTranslatePasswordWSResponseDTO',	'//sg00cbgtcssc01/sg/out/processed/Config',	'//sg00cbgtcssc01/sg/out/processed/Config',	'//sg00cbgtcssc01/sg/out/processed/Config',	'irn0JMYI0jDLocYdjbc5UPacPPac4VYfam0THUBt',	'CD7zYIAZeZ6gUsxbMJyhRYiY165cAjWfoQYu9JKO',	'//sg00cbgtcssc01/sg/out/processed/Config',	'irn0JMYI0jDLocYdjbc5UPacPPac4VYfam0THUBt',	'CD7zYIAZeZ6gUsxbMJyhRYiY165cAjWfoQYu9JKO',	'findUniquePcCodeByEntityAndSecurityGroup',	'findUniquePcCodeByEntityAndSecurityGroup',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',	'findUniquePcCodeByEntityAndSecurityGroup',	'findUniquePcCodeByEntityAndSecurityGroup',	'/1rNXepmSbmeStY4lOxL4kulRWrYvuK2NgsYjWPl',	'TargetTrackingScalingPolicyConfiguration',	'MadameMarketingPreferencesUpdateResponse',	'/getDefaultConsolidatedProductPcCodeData',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'TargetTrackingScalingPolicyConfiguration',	'TargetTrackingScalingPolicyConfiguration',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'OfflineMessagingRetrieveOMSummaryService',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'/repository/FPPC/com/dbs/binary/gradle/5',	'/repository/FPPC/com/dbs/binary/gradle/5',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'accountPlanKeyOpportunityDetailsFormPage',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'/nexus/content/groups/dbsrepo/repository',	'getAcraInDirectOwnerShareHolderCorporate',	'com/v1/cb/account/sg/gapicb/casa/odLimit',	'/service/rest/repository/browse/dbsrepo/',	'/service/rest/repository/browse/dbsrepo/',	'/service/rest/repository/browse/dbsrepo/',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/repository/EVOL/com/dbs/png/k2f/1',	'findUniquePcCodeByEntityAndSecurityGroup',	'/getDefaultConsolidatedProductPcCodeData',	'OfflineMessagingRetrieveOMSummaryService',	'accountPlanKeyOpportunityDetailsFormPage',	'OfflineMessagingRetrieveOMSummaryService',	'OfflineMessagingRetrieveOMSummaryService',	'OfflineMessagingRetrieveOMSummaryService',	'OfflineMessagingRetrieveOMSummaryService',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'/nexus/repository/EVOL/com/dbs/png/k2f/1',	'f47393e440840097b55fe1699014749baaac4901',	'f47393e440840097b55fe1699014749baaac4901',	'/nexus/content/groups/dbsrepo/repository',	'f47393e440840097b55fe1699014749baaac4901',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/content/groups/dbsrepo/repository',	'nexus/static/rapture/resources/icons/x32',	'/nexus/content/groups/dbsrepo/repository',	'8443/nexus/repository/EVOL/com/dbs/itss/',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/content/groups/dbsrepo/repository',	'/aheadincloud/awscertchallenge/mechanics',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/content/groups/dbsrepo/repository',	'/nexus/content/groups/dbsrepo/repository',	'TargetTrackingScalingPolicyConfiguration',	'/nexus/content/groups/dbsrepo/repository',	'TargetTrackingScalingPolicyConfiguration',	'TargetTrackingScalingPolicyConfiguration',	'TargetTrackingScalingPolicyConfiguration',	'TargetTrackingScalingPolicyConfiguration',	'checkEmailValidateWhenOldNewEmailIsEqual',	'TargetTrackingScalingPolicyConfiguration',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'8443/nexus/content/repositories/SOD/com/',	'com/api/customersearch/SG/C042912006Z00/',	'/nexus/repository/pypi/packages/fastapi/',	'/nexus/repository/pypi/packages/fastapi/',	'/nexus/repository/pypi/packages/fastapi/',	'/nexus/repository/pypi/packages/fastapi/',	'SharedResources/WSDL/Concret/ActivitiSvc',	'SharedResources/WSDL/Concret/ActivitiSvc',	'/nexus/repository/TDVO/com/dbs/itt/oapm/',	'SharedResources/WSDL/Concret/ActivitiSvc',	'SharedResources/WSDL/Concret/ActivitiSvc',	'SharedResources/WSDL/Concret/ActivitiSvc',	'SharedResources/WSDL/Concret/ActivitiSvc',	'AddrEnquiryRequestJobInterfaceDataMapper',	'AddrEnquiryHKIDRequestInterfaceProcessor',	'testMapBioReferenceResourceAfterCreation',	'testMapBioReferenceResourceAfterCreation',	'testMapBioReferenceResourceAfterCreation',	'js/plugins/datatables/buttons/dataTables',	'testMapBioReferenceResourceAfterCreation',	'js/plugins/datatables/buttons/dataTables',	'js/plugins/datatables/buttons/dataTables',	'mockMadameDocumentDetailResponseFinCheck',	'testMapBioReferenceResourceAfterCreation',	'testMapBioReferenceResourceAfterCreation',	'mockMadameDocumentDetailResponseFinCheck',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'testMapBioReferenceResourceAfterCreation',	'retrieveBioReferencesByListOfProspectIds',	'accountPlanKeyOpportunityDetailsFormPage',	'testMapBioReferenceResourceAfterCreation',	'retrieveBioReferencesByListOfProspectIds',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'DBSAccountPlanDetailsEditDraftPageModule',	'findAmbsCustomerNbrOrderByAmbsCustNbrAsc',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'findAmbsCustomerNbrOrderByAmbsCustNbrAsc',	'accountPlanKeyOpportunityDetailsFormPage',	'accountPlanKeyOpportunityDetailsFormPage',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'sendMessageRequestInterruptWithVariables',	'/reducers/accountOpening/receiveCustomer',	'branchconnect/device/lib/hooks/useDevice',	'lib/components/AccountSearchV2/constants',	'lib/components/AccountSearchV2/constants',	'lib/components/AccountSearchV2/constants',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'sendMessageRequestInterruptWithVariables',	'/reducers/accountOpening/receiveCustomer',	'branchconnect/device/lib/hooks/useDevice',	'lib/components/AccountSearchV2/constants',	'lib/components/AccountSearchV2/constants',	'lib/components/AccountSearchV2/constants',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'getPostPricingFieldsForDocumentationTeam',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'/2uNUMNVR0Yc+zp4R5eHgWJTWUmZriXRGZQY+JtI',	'/2uNUMNVR0Yc+zp4R5eHgWJTWUmZriXRGZQY+JtI',	'/2uNUMNVR0Yc+zp4R5eHgWJTWUmZriXRGZQY+JtI',	'/2uNUMNVR0Yc+zp4R5eHgWJTWUmZriXRGZQY+JtI',	'/2uNUMNVR0Yc+zp4R5eHgWJTWUmZriXRGZQY+JtI',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'8443/nexus/repository/ITSS/com/dbs/itss/',	'AddrEnquiryHKIDRequestInterfaceProcessor',	'AddrEnquiryHKIDRequestInterfaceProcessor',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/'
                ,	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'com/api/customersearch/SG/C042912006Z00/',	'MultipleBinaryClassificationModelManager',	'/cbgba/databackup/onshore/common/sasops/',	'MultipleBinaryClassificationModelManager',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'MultipleBinaryClassificationModelManager',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'projectDetails/getAuditReportDetailsById',	'createCardDetlInqResponseCardDetlPinDetl',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'createCardDetlInqResponseCardDetlPinDetl',	'createCardDetlInqResponseCardDetlPinDetl',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'generateBicAccountHoldingInstitutionList',	'dbs/itt/sdwt/camel/routes/RouteConstants',	'mockMadameDocumentDetailResponseFinCheck',	'io/docs/ts/latest/api/common/index/NgFor',	'io/docs/ts/latest/api/common/index/NgFor',	'io/docs/ts/latest/api/common/index/NgFor',	'branchconnect/device/lib/hooks/useDevice',	'branchconnect/device/lib/hooks/useDevice',	'io/docs/ts/latest/api/common/index/NgFor',	'io/docs/ts/latest/api/common/index/NgFor',	'io/docs/ts/latest/api/common/index/NgFor',	'io/docs/ts/latest/api/common/index/NgFor',	'2iZxXf3QLGSW7o4ihwCfKEISDYV338+4voFkM9Eq',	'2iZxXf3QLGSW7o4ihwCfKEISDYV338+4voFkM9Eq',	'TDSViewLookupNonIdeal/tdsview/qmsService',	'authentication/verification/saveOrUpdate',	'Y3PxJp5bJ9kjRctIHhexajLZHseq3RnHwpvZTjF5',	'TDSViewLookupNonIdeal/tdsview/qmsService',	'1ePEsr5yh3AM/MutPRexr+xpxESuhDMDHi2dnGom',	'/TxR5QSihastAvZvhBvLNA6f64vSOi8oLu8EhilM',	'/TxR5QSihastAvZvhBvLNA6f64vSOi8oLu8EhilM']
# print("opt" in words_list)
print(len(strings_to_split))
count = 0
for i in strings_to_split:
	x = list(chain.from_iterable(string_splitting(i)))
	# print(x)
	for j in x:
		if re.findall("[\d]",i):
			if j.lower() not in words_list and len(j.lower()) >2:
				print(i,"Valid")
				count = count +1
				break
			else:
				# print(i,"Invalid")
				break
print(count)
with open("new2.txt","w+") as f:
	for i in words_list:
		f.write("%s\n" % i)
