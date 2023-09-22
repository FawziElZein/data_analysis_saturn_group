from enum import Enum


class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    CREATE_TABLE_ERROR = "Error creating new table"
    INSERT_INTO_TABLE_ERROR = "Error inserting into table"
    STAGING_DATA_ERROR = "Error staging recent data"
    CREATE_STAGING_TABLES_ERROR = "Error creating staging tables"
    ETL_CHECKPOINT_ERROR = "Error creating ETL checkpoint"
    FUNCTION_NA = "Function not available"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"
    HOOK_SQL_ERROR = "Hook: SQL Error"
    DATE_CONVERSION_ERROR = "column is not a date format"
    RETURN_ETL_LAST_UPDATE_ERROR = "Error returning ETL last update"
    

class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    
class PandasFunctions(Enum):
    REMOVE_DUPLICATES = "remove duplicates values from data frame"
    REMOVE_NULLS = "remove nulls values from data frame"
    GET_BLANKS = "retreive rows having any cell with an empty value"
    GET_SHAPE = "retreive dimensions of the data frame"
    GET_LENGTH = "retreive the length of the data frame"
  
class PreHookSteps(Enum):
    EXECUTE_SQL_QUERY = "execute_sql_folder"

class SourceName(Enum):
    DVD_RENTAL = "dvd_rental"
    COLLEGE = "college"
    SUPER_STORE = "super_store"

class CsvUrl(Enum):
    Tweets_About_Big_Crypto_Hack='https://www.kaggle.com/datasets/marianna13/tweets-about-big-crypto-hack/download?datasetVersionNumber=1'
    ELON_MUSK_TWEETS = 'https://storage.googleapis.com/kagglesdsdata/datasets/3563626/6206522/Emusk_2021_tweets.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230920%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230920T144512Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=33c16d7667b7d7b016856e3955505b7261e058d88c026b6586cba7c78b30feda5839a21220bd5d29a69e73a978711eac8d92d908cc08005c72ad6535a9a545f64f852e814f8fcf89e9468834fbfcfe7119470bcc1c119553b86e3f8c6554b3df4f83a34df0558904041585a32c9f0ad5b349558e78f15b25eb2179a842feec84c90c2eade403058bec18c5b3491460fbccd91d166d9f912ec36599b3cc7cef9fe7945d98fc3ba56adf75c27af5b5e7a2838408da40e4692f7603ecf5ccbd27f1ac347291fa23b6be83e8581828915be54f02651fed30ff1d70a02befa2d39138d80205218f0424b274b6119b40f8d94b31d0cb7f8721144511e2df5434dc25a0' 
    BITCOIN_USD_HISTORICAL_DATA = 'https://www.coingecko.com/price_charts/export/1/usd.csv'
    COIN_AAVE_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Aave.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T082525Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0f640c762aa89eec3b30480077b4b2f6f58f52b50dfe553612c38823b5e57f0f6f73524d7f1c9e24e42e1d0d826f71106ebb6c02c56bf66461688ed53da3920521d7f3552c1815728a8ec7b5eccc07756276d33958cda3f9a319aea9016b9fdd8effed64de3fd35635ebf06e6436be508e1d5cd91f828d1a27509059c5f3819122123625af0da1b3d5501eba33c336518f7ad28d793472ba69924f2f20698ceedb5c580e86d8cba1689891bc948f6a9438d359b8f922b919e19b3405d590b20339184b329e0ce948a18499089af461bd1aa2aca5830547db42563817ec93bf3c2823ffda39300b1d038028efeda1e15e268bfd007b864f7a31145100fe7eddb8'
    COIN_BINANCE_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_BinanceCoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T083745Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a8003cfbb44abdb8158226c2acec25e9313062c8a68c2b25d1d5409691becbe4b4d187bb29fcfcc40b22a923e35292a8e99b3079a8216f83e97b30cebf6c988457ffa18c6d2ac50a65fb929374ba2a2b47b6a97f402f869d40cba45ba11b1c91a38e6a1a560b835e715823c7d1df76f55791fd8680ce2bb14546a344076afeea7973429fba5a3d3289256d382c9e13ed3a1fe76c35599b33efa3b8517a3dafefe65068ef185071277ac63afd1b72a5fba5e26f611cb6a7cd013051e1f39d62256c2af57f381d58397e14fa4dac261832d10229ccfcf4f3eedc11bd78f7d26a9fd9dfeb96e3420a4701da4febf6072bc334458647762a5d4264ffe157323bc2f4'
    COIN_BITCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Bitcoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T083904Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8781978ad73dd7c8f1395cd10b8c1b2783c60f69a1c2a758ee414c80f645485e3008853bf993fa6b2288210726ba97480a878371267220b887898c8c50df42452c6f9b365bf72eab92f4f49e59527631957ffb506b4a2b7e790f37b41bf5e1d05628d82d6e6fed8f281f1c6aa50f6b6fa8523803c0aa9f7c9d84fc0507f3e210ff11f99b854df1396da4986c754b68b3cae56d20e6b6dc5485d119360ae89869040a8869110f4663980243e1471c8ea51aa2826ed3ce4251e26cba081f158ec238b9c1c27af92de84df766409a548115480cae189d27a1f352d8a60146a7f5fb7eea11259a3f1b5b3c07d279970c90e78d5ba61c2af027a37305f6cf25f4123f'
    COIN_CARDANO_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Cardano.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084452Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=47c0fc73cd37d469cca761958a9ac9de5654e7243f9e6d22a8420b4d0a9b916d3bfe378d6599be36096f81a56f313a66d480e9f0e8cdb57166ab6716647ee09d0a6fa566eb1136e689024492eea6ebc5c414efc7e5e959c1fcdc38b6c7fb201c34e83ff5067dc06cff69fddc880d8ff248ce5f478fab0fd6e3ce48c051afe9d8629db3fcf3a131ef0e80354e4bd0c11f18b3a4adb2bd000f0e157741f318c07b630bf5815ac10a72bf4a503d1142fd902f03eadcbb02b277955d2ec94216b187f6c5ad645a394aa3c78cb656ba67953fecc5f6b5f46c8f802766b2fe5df036480e0f3c1035585793ae3ad6309459e1c819d4fb317af79a7878c44bc100d958f4'
    COIN_CHAINLINK_USD_HISTORICAL_DATA='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_ChainLink.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084631Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=c9b7a73330e4d691e9004b39923c53b2385a00e70ced80520da74db75427f350f773e8e5c6009dd33d65124aebe1d0ef13c4a2df8369fb196734b52fc6d240808114d32bd21472ef0f56d05f2715d72f7211f2fd5f4e268538025b6527bc47a00d31d0f4bc7ac9d4a8fd1d83f2d920064709e35d95e4fb077b9a0a434fabffd38460068188943f9a704984f595635f971eeacc5cc50ef8999dc5979de13fb4844526570c9ab51e0e67ffab8462a71e8d14f9b1988cf0d794e83414134439f4c1ceec297f597b37e6b6077480e6cb2241802f16dd17948b1e5d984490621f944a63d5343c2854dd99c1d41c1b0521442085c56e3e5c35d0171fb0ed8abf03b14e'

    COIN_COSMOS_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Cosmos.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084659Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=bbc7610e786b71fc34d3236a2c3145dea4429159c0c7f73cc41394e42537edb2c7803bb34e80790c5cecabf668695c6c3655ed95d59fa8ea0246dcb634d3efadcbe5d3291d9993d75a145d6327617c7e5e6c3cee5a0dcf70cccb68acc1145f7abfaadff7a26cd8358ddd42cc451b2f7adb97133854de4b41547875bd0cfa7dfc657371aa234981ec80598ec95f32e940322f073a84bd83276046c5c4fe24507b8ce3e5811ee499b819bc87d6e9ac82b467c1cc323faa18e7d4223e1c318975e0c06145f8c3625153389e4541d716568c0b338fa924321ee2ae61610a562131f0a42c703844db3ee47640821452bac8ac4752f302da0d16036ec74e7184a03eaa'

    COIN_CRYPTOCOMCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_CryptocomCoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084733Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=087d437f5e1e063019958a8ccd65221890126db1114b5b5e158265d29262f1c42863df2365865f0785d232fc05904270376cdf280b07fdad9ed4ab2d87e024b831fde26e57969b8b3ffe5d88a8024e48b16a45b92091e4c77fa275577eb5580ebb1a531267dc29517f5af3b2790487d4621a8158aebeb8fe00e9140df928dbac5f2fd08f8e4191fc939660acd9de2e8ec0c79a40ba2922382724e9e669b3f20a8494d149db75d10239a5b87ccdba2340c16565e39fc6cd4911fc4a84aef5178a87cbd2408fb01bda88210f20c1fd0b5a8c06706e68ea3d75736a9b6d1d50612c186cd081c157aba271adbafa2828c4818ae7a43ed80226c13c04e52e4256b3fa'

    COIN_DOGECOIN_USD_HISTORICAL_DATA='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Dogecoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084811Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=54d3218dd862ff322fec280ad4e736247a623f93d574b91f77650247ba7ae662e5f6384692dc9fcd53afb305b8b57068f773c564c746ea199c6696300a2cb33bceb94abf38ce7f3eee7daa576c68db66f89272366736f6eaad0f3c05f7c1d84e77a12f25a3ce5176ee5ba123e5d3b57b749b09f379476a5206390bd94720a0c55df721c3a613940fd1f250dd4635939aafa10f09140e99740febb99f6c4f283bb36f7f39e058548fd74a89ef1041bda5872223524f2b58d86cd12234cc361611a952fd1ceec75e3964a0bcc8ec86259c5c20a23e375214a45567a2d27660e5abe81e7221b3be0ca204c7293e8dcc7c7fc78d10e109e8330725919f0fe078f2b1'

    COIN_EOS_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_EOS.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084903Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=46a903f49abbdd35993aa333df76b6803ac7c71a13779b773db5ed875a2c95341e050901c7a50d3ea9eaf45a5ba525155b6876e305110eb420524fcc7e7c5ccad89b0c3a23a81a10e10b9d835903ec7440ca3c224ca93f97981b34d1bc5e92f8ed6b459595136f56fff8fe696df1c74c6e748e270c666b95256e3fbc14881e8e55203333f4cdd226f4a5c7040538867bec7f8aed83856c9f754bb895c09c461020bc8611d8db174aa54f99238633a89f65d534eb58243c3d6df68a2efa7b2a052be67f67407521d2aa8e865c796f3657d859b9d0971c8fe3c66371b887e0ba6935566e1374c001b38096e66bd82928411ba072e6657a98f1b19a39c1720a93ef'

    COIN_ETHEREUM_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Ethereum.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084931Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=672dda863e531cb7091aa1aa855bc698723e40205426341b2d6fa420a937b50f7e222d8047e004f6121c7431ed26f91253be0ca818b0be5ab74cbfcbf0f65aa5378103650f1216d1816a8e35d3ed82db06b232d2bdfac4ea8dc743294f03740c9c0d49f204a0e34ffcb6faa2c38abec78999f7f096443c34f16d28736fa2c0f1940c404b5a313e441d3599f253def97f5700e03fc62c13c59cfe3ea747fcbd17ef52a71fd5fba7ffd33cc41201995e2a0605b34613544d13b31c2f54ba31c95b5009d5abd3e7db0b80a1c916ec6f376c04970bc39e76cb825ea4bb0d6367f375ced370147cfb9e3888680cc38fab9373ddd801e9515b1cb31269223e2c99d0c5'

    COIN_LOTA_USD_HISTORICAL_DATA ='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Iota.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085019Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=334bebb1278d05eb4ef6d49b262c717c6d43ebc25a0b04b1f6a0ed0232865065542208db096f30de89838ac411983f40e6cbde3a50008b3cd2968a289632a5cc901aa4c82ba609c9314768a7173aa433c727c18cb8d09e3c0a2a40173a4606e84d02a5a713dace53d434fe1703755835648720d85e2785b2d0b8b4519398f4845a9a7a201b82e5613583c56fa07991150310ccd010285901eee999961af7aae31f2a2e3701ecab854cf128d429e6579bc3b3ee4925fe60633709260546c0e7a3ad6a8ce9dc862d77466a4f6c6ce6ed165760e6c165ea2568adf78cf4373c6c697104af21700ffe297188e20ab045bf4add7151f62ef386bab59f8dab2cb43591'

    COIN_LITECOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Litecoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085045Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=4581d013b438f2c87e2156824e3dafb13a390324191759cdca3c32cccd55dbb50bfd23dcfc2fd8b12b7751081dbdb3a8a2c0bba5f1cdd83cf52d16e45e683849cfd4ae5fa36e040882592887681f7c5a8446b6aa7f4e4c83fe852c28a62e076b62ba23c8c66d164cef987732e3a7ef399467cb58cbb1b0c28d3ea6ed81fe0593ce22368a6d025ba9c8d13568f569ec145451a7f70d4369f06b4b847538b88f7709a02e8efafd3e98c6eb3137fbbb0bb2e5f6286e678b8bc6314a15ea9076b8ad051eb809036eb2bc2adb972b5df5431e9fba4ccd4d966e9603c912064d0e10bbec9be860e97343dbb28398dffb0bf66100ea0b7c7ac370e5d19b63144e86435f'

    COIN_MONERO_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Monero.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085122Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=b785ec0d41796661051bcea8e37a407b436a008383a4c9b7c13c8c6c5e296a7f2dced3b253e6818a1cc745edabc0b0518b5a1b3187d67014ecbc0646e124050f255dfd38945d4f3300c75e86b8ccf23a28fe171bc43ce5020dd2af43b6bea90b081d5cb4d18dd5cf9c14f3b01d090b764af2f44e64ecbe2e856e4b72c9fa086ed8d2b57638275c976adc9d15b5174a2f096a06abe080df3b19f970313db2ba05d43193a78bdc0f7888bdf0fe362045efdc70754ee7b935682b8455dfdf475efb520d5dc2235cd688921c2718eb774acf9a47ea2b3ebd7645e4bb6925115c0e7a8c1c165951a5848449ac06fe675e70332fdfbd7f8b15324235f308b8a17c96ed'

    COIN_NEM_USD_HISTORICAL_DATA ='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_NEM.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085232Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=90b23cfd18ad7a25680e726231b24da40a900916b37aae9bd7cd67154f2ffb0fb552370a73d75c6a95634388bdedf7f22d16ec370a308332089673d69599641a9aaede589b3f7cf862152f04e5e1f8bb827e5b2ce5058698f988f6a053992f878c61daf86d784189030dd4bbee9a7e4b62dfce235f55278c3ce83a1229a6f34fde4d0a69e4604a8ffe87f649aa698d8fd2b3d3be71703b9c638997c9275f510e6ef91fac8766324f6040dfcbf38a90a52aac8bb416e8eb6700c638c0f92f49d6e8064bcd0d6d411b94e5356435bfb819308199b6818bef3bfd494f95ab61605f03d9b1455b38c3acf21f1f444e3b1acd054dd70bec7582510688eb9da68c5f98'

    COIN_POLKADOT_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Polkadot.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085259Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71b4f59d213e525b37d0cc48474ac9bdc78cf9c2db0fe08b5140697c9817e7ac97f9f10ef9079cf8e56036f19e0e7b8e8f4474ebcfa5aae7418874d5a438f714c1f3cc2d9932a3529f1d70014ce68a9dd5c89cf360880c39676cd8bbfe1bf261e6169f8bd7e228d6b40fe852272cff25cdbfa1b6241fbc5784e2158dc058015d97cd9fd2d29b303ac544fd72f978d2b9c89874094899cb3390ae1d7ff6aae0bad334aa02bdf20868c8eba7c5174ac71dc3fd78f360242dd0ce6924c84c3b02a37926911c8a569e8cdf57b14d529ce32eab9da7f4fb35ac0f1e15517c1179512217cef6714f6feb8fee22c32c40bcd145d934201e166915ae9584ed33e7e1c9e1'

    COIN_SOLANA_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Solana.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085342Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3ec013761f77401dd459e3afd18f0fa78da8603736c70b43ad43446e11b7a548297f40e83e7d5718068685471818670e5a9470f39a359f7f9bade3885d11996d437c6322e1e441fa2e5f1718dc1917922845844d0552b5038b34a41345ef9906d5750c87e70ea9a8b42afa9e6c5c7c584fb3e109dd509c8e1e0e245c33ef1a8ebb1481d08f5ffb06643c03f95708bc66c18b50e3f1025ee8f36e1083f2b6d6b223916dd07f0356ded5dc6a139d25d79817bbebdea3e4f4f8ab92727e0ddb3fd8583c2a48b67a2bf3612c0d6a1dd8d5028e2e86b13c8e462f983353509c3dc127969c612d16d6f0b59b1b356f511e2436e424bddcb24c58e651d05d3eb813ef85'
    
    COIN_STELLAR_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Stellar.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085417Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8e38035a512a5ddc5444f02154c17a7854fbd8b33515216ee9eb0565d91afe713c21a48c7386fdab4d896ae1ef7f9891d78d5faa3d8def557fc35165b960e1af0d5ed1f2db58b26ba11a424d360c1314a0bcfc0aaf47573257fdd3046cb806ba189acd8f468ec3e024903e0a93b63587d1d5703b528503391246968fb68d4fb6412f351a5964609f75eebd412345789e62f2d3165c5a2c4a8992e7e33387d56fdd9f36aca4a25424397c190f5efc14c33ff581ddbab5eabb584e9f02dbeeff42bb1d4d2fe888b34014cd7e4e26f4b1425a64e666b832b3259c07581b8328abbdde1442376a91220fcda9192128efa49330ebcc9101a90e90695e09840578e65f'

    COIN_TETHER_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Tether.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085441Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2499f5c0a1c40e43767d5cfeb8403fef4834c4dadf929cdc44874149d4de08bb88e8c064b1ac817566043878797c2105adb5cc9dcb62a918284d0cc348831aae17acab71831fd728729a2c1525dbf468ae569621c3a24825fded7691526ac4a4af8cb964d8b7674e957dbe870e86e280c97e8efec3e0f0cb85c225451df3cf2f5e12b5c789827c267392e967f4dc8799e778e0bfb270d3f54334ad55073e431252bea88694bda6f9b0ba12bb4665599a880cef64fd975faafe7a262795bf3009afc5e32fc8de7a023aac801a5b9c6b1c71749ee12fae7661b8123f73f8104e3c5511236bd25b992daa0fb22d48df18c339f99e9fc683076f78054ec4fcfb9c94'

    COIN_TRON_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Tron.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085506Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=73cd74451b90de07d1406618bbaadfba46be371e4fcfe29c25c21aee5040e57d8a4595f00677dd938017da1a90259e74fa9091bbd7f1aa57c425c62e5e7728ae5f11200fb44949a481d446bcd87918f0dd4c871f861c5985d6a34bb0484618ea73cb9def9abe5e3af5b8a13695c4169fa113caaa233814f53d132f6e49392fb191dfc8172dde157555bb4d6ae3f3954fcdb8e5847c8b6d60b80428533dd64a422e168e3611e07ff90e7995ab9ed6a74329db8711553a86b6b5e74cd0817357998eb90f85df1160071d8b91a28b3376578b7df93e324d784502e7883660bf0a9965f47285a23f8d51857a18bab72f64c5beadfa6043ad3044cddb6afa8bb9725b'

    COIN_USDCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_USDCoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085529Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=ce855806bfc18d56be1247329894ba41e9329f0ca7b3a43559540e7492ad3a9fc1a10aac254b6325f43e592296fbdeb95726bb4c2ca65c732bc4fd79b7e14ca47f3103670a4ccb588737ac94c4f3ffa70e4ed5d6d389ec7697431bf47b988ec159ee20cf05c0520aeb761df4ee99ac6017568a337022c645f6f8483724663d91dbd8df130c5a5ae630ffa5340c3ce5b43d7059830eeb5a7fa4057cf124cf1ea604f55cbc778e126c1bdb2f266fd9f9aefc276c6ddfba50845a9c8fdd177f6886610a5cd3cca4efec5e70abb98ece7fe774b5960104d13ff0c603895874af83c4d3aa4bba7519736a0632903b95789ca98803d03a5cfac8da2d777f72b0fb7140'

    COIN_UNISWAP_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Uniswap.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T091116Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5ba75c0da083670f3656c077e07b0252cd8c1d243056c8bdf25308577f06a63f85c8b62ee20764cd60dfde97c29acf43db03355af419a3863f30cb07deb4953603e583e038bffc0fb07ade26dd0187fd62a85cecf22d3a5e9a33a7cf6908a27a66ee07b42fdee87b51d407ffca65030be6f9e93af3637adeab3a8b720a0ea5a38ae098042371ecdfe1c3d3c522663cd00f62dbb26de907e314c0375f669804293b2777276cdc35ab3ea91516a2a74cd9f0564b3ffa0947632e3896032651eda4bd9503e3cddba904672d6eb79d7868d30f02007581f116123525ae3fec9b1b94761caff90dfb700076c48406ac313fa70a283be91033094d49dd1d88bc630cbb'

    COIN_WRAPPEDBITCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_WrappedBitcoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T091152Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a7cc33b8834f3f75ecbdd8b5cf25b7c8122c16cb5c65cacb44fa542ca5c4012c5b13aa27669ded62fc68156429326da1e2755d2db91375deef0bf6172be884c57b8470a7e9bf9d6eba73c2f60e29ded7c3164653ce9c0f54bd83e2f57ec475b040882441d4d198202c36dd8467c9330300bb337aabe380c7a278964bdcfdd49ebfd7a212a29a1c66acd322557ca9b74b16d93cbe6623f77bcf2204b4b9b32f12cbb9da43dc5fcf2894166acba23a15e5e2906aa538cff1d8fa325438692089f56c8974cd7c552426ec6ca4aa7c1ebe8abb0925d858f9cc304aaa69c658a24024b5cec49356367a4d3b5eb8d94bca4a5574de6ec59e9c5094cf3cac3ee3aed724'

    COIN_XRP_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_XRP.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T091259Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0dffde001c58816d3586e4c5d50a025f798b3076d8547da384c7162db5f81a25faf6ebcecf265bf7cd48b74b039ae57e8400e02449239dfbbba5a00ef16335105f4dc77ce69d66eb2d1bce7ee428ed2891391b002bb93d39cb1d375efa6d1c25ea8dbf700d2b4ca2575a4b54d0cb4ddb4fda7b8a85b116b826befe274df80a4032dd9ae82c9bdc3d0b1d4a3521fc95ae3ade8bbf701344df0f23bf19f6c17aaee30c7f2c4079ac4cb6b6998b24c09c001ce24539ed5c8223c32aa75758906eda79880e5ce4c97959a72f96950dfc2540bee72faf0c64667c498901c6f2bdc477f23940e376954fab744cf4c9a4168ce58cd588a5a386cc812b43805fe1234279'
    
class SQLTablesToReplicate(Enum):
    RENTAL = "dvd_rental.rental"
    FILM = "dvd_rental.film"
    STUDENTS = "college.student"
    DIM_CUSTOMER = "super_store.dim_customer"
    DIM_LOCATION = "super_store.dim_location"
    DIM_PRODUCT = "super_store.dim_product"
    DIM_SALESPERSON = "super_store.dim_salesperson"
    FACT_PURCHASE = "super_store.fact_purchase"
    
class IncrementalField(Enum):
    RENTAL = "rental_last_update"
    FILM = "film_last_update"
    ACTOR = "actor_last_update"


class ETLStep(Enum):
    PRE_HOOK = 0
    HOOK = 1

class DestinationName(Enum):
    Datawarehouse = "dw_reporting"

    class ETLActionType(Enum):
        FULL_REFRESH = "full_refresh"
        IncrementalField = "incremental"