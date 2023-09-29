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
    CREATE_INSERT_STAGING_TABLES_ERROR = "Error creating/inserting into staging tables"
    ETL_CHECKPOINT_ERROR = "Error creating ETL checkpoint"
    ETL_INSERT_CHECKPOINT_ERROR = "Error inserting ETL checkpoint"
    ETL_UPDATE_CHECKPOINT_ERROR = "Error updating ETL checkpoint"
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
    HTTP = "Http"
    
class PandasFunctions(Enum):
    REMOVE_DUPLICATES = "remove duplicates values from data frame"
    REMOVE_NULLS = "remove nulls values from data frame"
    GET_BLANKS = "retreive rows having any cell with an empty value"
    GET_SHAPE = "retreive dimensions of the data frame"
    GET_LENGTH = "retreive the length of the data frame"
  
class PreHookSteps(Enum):
    EXECUTE_SQL_QUERY = "execute_sql_folder"



class CsvUrlCoinsInfo(Enum):
    COINS_INFO = [0,'https://storage.googleapis.com/csv_links/cryptocurrency-coins-data-info.csv']

class CsvUrlTweets(Enum):
    ELON_MUSK_TWEETS = [0,'https://storage.googleapis.com/csv_links/elon_musk_tweets_clean_data.csv'] 

class CoinsEnergyConsumption(Enum):
    BITCOIN_ENERGY_CONSUMPTION = [0,'https://storage.googleapis.com/csv_links/btc_energy_consumption.csv']

class CsvUrlHistoricalData(Enum):
    CRYPTO_TRANSACTIONS = [0,'https://storage.googleapis.com/csv_links/dex_transactions_post_cleaning.csv']
    CRYPTO_TWEETS = [0,'https://storage.googleapis.com/csv_links/dataset_52_person_tweets.csv']

    #minified version
    # CRYPTO_TRANSACTIONS = [0,'https://storage.googleapis.com/csv_links/dex_transactions_post_cleaning_MIN-Version.csv']

    BTC_TWEETS_SENTIMENTS = [0,'https://storage.googleapis.com/csv_links/btc_daily_2021_2023.csv']
    ETH_TWEETS_SENTIMENTS = [0,'https://storage.googleapis.com/csv_links/eth_daily_2021_2023.csv']
    DOGE_TWEETS_SENTIMENTS = [0,'https://storage.googleapis.com/csv_links/doge_daily_2021_2023.csv']

    # COIN_AAVE_KAGGLE = [0,'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Aave.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T082525Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=0f640c762aa89eec3b30480077b4b2f6f58f52b50dfe553612c38823b5e57f0f6f73524d7f1c9e24e42e1d0d826f71106ebb6c02c56bf66461688ed53da3920521d7f3552c1815728a8ec7b5eccc07756276d33958cda3f9a319aea9016b9fdd8effed64de3fd35635ebf06e6436be508e1d5cd91f828d1a27509059c5f3819122123625af0da1b3d5501eba33c336518f7ad28d793472ba69924f2f20698ceedb5c580e86d8cba1689891bc948f6a9438d359b8f922b919e19b3405d590b20339184b329e0ce948a18499089af461bd1aa2aca5830547db42563817ec93bf3c2823ffda39300b1d038028efeda1e15e268bfd007b864f7a31145100fe7eddb8']
    # COIN_CARDANO_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Cardano.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084452Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=47c0fc73cd37d469cca761958a9ac9de5654e7243f9e6d22a8420b4d0a9b916d3bfe378d6599be36096f81a56f313a66d480e9f0e8cdb57166ab6716647ee09d0a6fa566eb1136e689024492eea6ebc5c414efc7e5e959c1fcdc38b6c7fb201c34e83ff5067dc06cff69fddc880d8ff248ce5f478fab0fd6e3ce48c051afe9d8629db3fcf3a131ef0e80354e4bd0c11f18b3a4adb2bd000f0e157741f318c07b630bf5815ac10a72bf4a503d1142fd902f03eadcbb02b277955d2ec94216b187f6c5ad645a394aa3c78cb656ba67953fecc5f6b5f46c8f802766b2fe5df036480e0f3c1035585793ae3ad6309459e1c819d4fb317af79a7878c44bc100d958f4'
    # COIN_CHAINLINK_USD_HISTORICAL_DATA='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_ChainLink.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084631Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=c9b7a73330e4d691e9004b39923c53b2385a00e70ced80520da74db75427f350f773e8e5c6009dd33d65124aebe1d0ef13c4a2df8369fb196734b52fc6d240808114d32bd21472ef0f56d05f2715d72f7211f2fd5f4e268538025b6527bc47a00d31d0f4bc7ac9d4a8fd1d83f2d920064709e35d95e4fb077b9a0a434fabffd38460068188943f9a704984f595635f971eeacc5cc50ef8999dc5979de13fb4844526570c9ab51e0e67ffab8462a71e8d14f9b1988cf0d794e83414134439f4c1ceec297f597b37e6b6077480e6cb2241802f16dd17948b1e5d984490621f944a63d5343c2854dd99c1d41c1b0521442085c56e3e5c35d0171fb0ed8abf03b14e'
    # COIN_COSMOS_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Cosmos.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084659Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=bbc7610e786b71fc34d3236a2c3145dea4429159c0c7f73cc41394e42537edb2c7803bb34e80790c5cecabf668695c6c3655ed95d59fa8ea0246dcb634d3efadcbe5d3291d9993d75a145d6327617c7e5e6c3cee5a0dcf70cccb68acc1145f7abfaadff7a26cd8358ddd42cc451b2f7adb97133854de4b41547875bd0cfa7dfc657371aa234981ec80598ec95f32e940322f073a84bd83276046c5c4fe24507b8ce3e5811ee499b819bc87d6e9ac82b467c1cc323faa18e7d4223e1c318975e0c06145f8c3625153389e4541d716568c0b338fa924321ee2ae61610a562131f0a42c703844db3ee47640821452bac8ac4752f302da0d16036ec74e7184a03eaa'
    # COIN_CRYPTOCOMCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_CryptocomCoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084733Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=087d437f5e1e063019958a8ccd65221890126db1114b5b5e158265d29262f1c42863df2365865f0785d232fc05904270376cdf280b07fdad9ed4ab2d87e024b831fde26e57969b8b3ffe5d88a8024e48b16a45b92091e4c77fa275577eb5580ebb1a531267dc29517f5af3b2790487d4621a8158aebeb8fe00e9140df928dbac5f2fd08f8e4191fc939660acd9de2e8ec0c79a40ba2922382724e9e669b3f20a8494d149db75d10239a5b87ccdba2340c16565e39fc6cd4911fc4a84aef5178a87cbd2408fb01bda88210f20c1fd0b5a8c06706e68ea3d75736a9b6d1d50612c186cd081c157aba271adbafa2828c4818ae7a43ed80226c13c04e52e4256b3fa'
    # COIN_DOGECOIN_USD_HISTORICAL_DATA='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Dogecoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084811Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=54d3218dd862ff322fec280ad4e736247a623f93d574b91f77650247ba7ae662e5f6384692dc9fcd53afb305b8b57068f773c564c746ea199c6696300a2cb33bceb94abf38ce7f3eee7daa576c68db66f89272366736f6eaad0f3c05f7c1d84e77a12f25a3ce5176ee5ba123e5d3b57b749b09f379476a5206390bd94720a0c55df721c3a613940fd1f250dd4635939aafa10f09140e99740febb99f6c4f283bb36f7f39e058548fd74a89ef1041bda5872223524f2b58d86cd12234cc361611a952fd1ceec75e3964a0bcc8ec86259c5c20a23e375214a45567a2d27660e5abe81e7221b3be0ca204c7293e8dcc7c7fc78d10e109e8330725919f0fe078f2b1'
    # COIN_EOS_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_EOS.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T084903Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=46a903f49abbdd35993aa333df76b6803ac7c71a13779b773db5ed875a2c95341e050901c7a50d3ea9eaf45a5ba525155b6876e305110eb420524fcc7e7c5ccad89b0c3a23a81a10e10b9d835903ec7440ca3c224ca93f97981b34d1bc5e92f8ed6b459595136f56fff8fe696df1c74c6e748e270c666b95256e3fbc14881e8e55203333f4cdd226f4a5c7040538867bec7f8aed83856c9f754bb895c09c461020bc8611d8db174aa54f99238633a89f65d534eb58243c3d6df68a2efa7b2a052be67f67407521d2aa8e865c796f3657d859b9d0971c8fe3c66371b887e0ba6935566e1374c001b38096e66bd82928411ba072e6657a98f1b19a39c1720a93ef'
    # COIN_LOTA_USD_HISTORICAL_DATA ='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Iota.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085019Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=334bebb1278d05eb4ef6d49b262c717c6d43ebc25a0b04b1f6a0ed0232865065542208db096f30de89838ac411983f40e6cbde3a50008b3cd2968a289632a5cc901aa4c82ba609c9314768a7173aa433c727c18cb8d09e3c0a2a40173a4606e84d02a5a713dace53d434fe1703755835648720d85e2785b2d0b8b4519398f4845a9a7a201b82e5613583c56fa07991150310ccd010285901eee999961af7aae31f2a2e3701ecab854cf128d429e6579bc3b3ee4925fe60633709260546c0e7a3ad6a8ce9dc862d77466a4f6c6ce6ed165760e6c165ea2568adf78cf4373c6c697104af21700ffe297188e20ab045bf4add7151f62ef386bab59f8dab2cb43591'
    # COIN_MONERO_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Monero.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085122Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=b785ec0d41796661051bcea8e37a407b436a008383a4c9b7c13c8c6c5e296a7f2dced3b253e6818a1cc745edabc0b0518b5a1b3187d67014ecbc0646e124050f255dfd38945d4f3300c75e86b8ccf23a28fe171bc43ce5020dd2af43b6bea90b081d5cb4d18dd5cf9c14f3b01d090b764af2f44e64ecbe2e856e4b72c9fa086ed8d2b57638275c976adc9d15b5174a2f096a06abe080df3b19f970313db2ba05d43193a78bdc0f7888bdf0fe362045efdc70754ee7b935682b8455dfdf475efb520d5dc2235cd688921c2718eb774acf9a47ea2b3ebd7645e4bb6925115c0e7a8c1c165951a5848449ac06fe675e70332fdfbd7f8b15324235f308b8a17c96ed'
    # COIN_NEM_USD_HISTORICAL_DATA ='https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_NEM.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085232Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=90b23cfd18ad7a25680e726231b24da40a900916b37aae9bd7cd67154f2ffb0fb552370a73d75c6a95634388bdedf7f22d16ec370a308332089673d69599641a9aaede589b3f7cf862152f04e5e1f8bb827e5b2ce5058698f988f6a053992f878c61daf86d784189030dd4bbee9a7e4b62dfce235f55278c3ce83a1229a6f34fde4d0a69e4604a8ffe87f649aa698d8fd2b3d3be71703b9c638997c9275f510e6ef91fac8766324f6040dfcbf38a90a52aac8bb416e8eb6700c638c0f92f49d6e8064bcd0d6d411b94e5356435bfb819308199b6818bef3bfd494f95ab61605f03d9b1455b38c3acf21f1f444e3b1acd054dd70bec7582510688eb9da68c5f98'
    # COIN_POLKADOT_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Polkadot.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085259Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71b4f59d213e525b37d0cc48474ac9bdc78cf9c2db0fe08b5140697c9817e7ac97f9f10ef9079cf8e56036f19e0e7b8e8f4474ebcfa5aae7418874d5a438f714c1f3cc2d9932a3529f1d70014ce68a9dd5c89cf360880c39676cd8bbfe1bf261e6169f8bd7e228d6b40fe852272cff25cdbfa1b6241fbc5784e2158dc058015d97cd9fd2d29b303ac544fd72f978d2b9c89874094899cb3390ae1d7ff6aae0bad334aa02bdf20868c8eba7c5174ac71dc3fd78f360242dd0ce6924c84c3b02a37926911c8a569e8cdf57b14d529ce32eab9da7f4fb35ac0f1e15517c1179512217cef6714f6feb8fee22c32c40bcd145d934201e166915ae9584ed33e7e1c9e1'
    # COIN_SOLANA_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Solana.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085342Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3ec013761f77401dd459e3afd18f0fa78da8603736c70b43ad43446e11b7a548297f40e83e7d5718068685471818670e5a9470f39a359f7f9bade3885d11996d437c6322e1e441fa2e5f1718dc1917922845844d0552b5038b34a41345ef9906d5750c87e70ea9a8b42afa9e6c5c7c584fb3e109dd509c8e1e0e245c33ef1a8ebb1481d08f5ffb06643c03f95708bc66c18b50e3f1025ee8f36e1083f2b6d6b223916dd07f0356ded5dc6a139d25d79817bbebdea3e4f4f8ab92727e0ddb3fd8583c2a48b67a2bf3612c0d6a1dd8d5028e2e86b13c8e462f983353509c3dc127969c612d16d6f0b59b1b356f511e2436e424bddcb24c58e651d05d3eb813ef85'
    # COIN_STELLAR_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Stellar.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T085417Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8e38035a512a5ddc5444f02154c17a7854fbd8b33515216ee9eb0565d91afe713c21a48c7386fdab4d896ae1ef7f9891d78d5faa3d8def557fc35165b960e1af0d5ed1f2db58b26ba11a424d360c1314a0bcfc0aaf47573257fdd3046cb806ba189acd8f468ec3e024903e0a93b63587d1d5703b528503391246968fb68d4fb6412f351a5964609f75eebd412345789e62f2d3165c5a2c4a8992e7e33387d56fdd9f36aca4a25424397c190f5efc14c33ff581ddbab5eabb584e9f02dbeeff42bb1d4d2fe888b34014cd7e4e26f4b1425a64e666b832b3259c07581b8328abbdde1442376a91220fcda9192128efa49330ebcc9101a90e90695e09840578e65f'
    # COIN_UNISWAP_USD_HISTORICAL_DATA= 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_Uniswap.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T091116Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5ba75c0da083670f3656c077e07b0252cd8c1d243056c8bdf25308577f06a63f85c8b62ee20764cd60dfde97c29acf43db03355af419a3863f30cb07deb4953603e583e038bffc0fb07ade26dd0187fd62a85cecf22d3a5e9a33a7cf6908a27a66ee07b42fdee87b51d407ffca65030be6f9e93af3637adeab3a8b720a0ea5a38ae098042371ecdfe1c3d3c522663cd00f62dbb26de907e314c0375f669804293b2777276cdc35ab3ea91516a2a74cd9f0564b3ffa0947632e3896032651eda4bd9503e3cddba904672d6eb79d7868d30f02007581f116123525ae3fec9b1b94761caff90dfb700076c48406ac313fa70a283be91033094d49dd1d88bc630cbb'
    # COIN_WRAPPEDBITCOIN_USD_HISTORICAL_DATA = 'https://storage.googleapis.com/kagglesdsdata/datasets/1869/2402293/coin_WrappedBitcoin.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230921%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230921T091152Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=a7cc33b8834f3f75ecbdd8b5cf25b7c8122c16cb5c65cacb44fa542ca5c4012c5b13aa27669ded62fc68156429326da1e2755d2db91375deef0bf6172be884c57b8470a7e9bf9d6eba73c2f60e29ded7c3164653ce9c0f54bd83e2f57ec475b040882441d4d198202c36dd8467c9330300bb337aabe380c7a278964bdcfdd49ebfd7a212a29a1c66acd322557ca9b74b16d93cbe6623f77bcf2204b4b9b32f12cbb9da43dc5fcf2894166acba23a15e5e2906aa538cff1d8fa325438692089f56c8974cd7c552426ec6ca4aa7c1ebe8abb0925d858f9cc304aaa69c658a24024b5cec49356367a4d3b5eb8d94bca4a5574de6ec59e9c5094cf3cac3ee3aed724'
    

class DestinationDatabase(Enum):
    SCHEMA_NAME = "dw_reporting"
    DATABASE_NAME = "crypto_db"


class IncrementalField(Enum):
    COINS_INFO = "coins_info_Launch date"
    ELON_MUSK_TWEETS = "elon_musk_tweets_index"
    BITCOIN_HISTORICAL_PRICE = "bitcoin_historical_price_index"
    ETHEREUM_HISTORICAL_PRICE = "ethereum_historical_price_index"
    TETHER_HISTORICAL_PRICE = "tether_historical_price_index"
    BINANCECOIN_HISTORICAL_PRICE = "binancecoin_historical_price_index"
    XRP_HISTORICAL_PRICE = "xrp_historical_price_index"
    LITECOIN_HISTORICAL_PRICE = "litecoin_historical_price_index"
    USDCOIN_HISTORICAL_PRICE = "usdcoin_historical_price_index"
    DOGECOIN_HISTORICAL_PRICE = "dogecoin_historical_price_index"
    TRON_HISTORICAL_PRICE = "tron_historical_price_index"
    BINANCE_USD_HISTORICAL_PRICE = "binance_usd_historical_price_index"
    CRYPTO_TRANSACTIONS = "crypto_transactions_Date Time"
    BITCOIN_ENERGY_CONSUMPTION = "bitcoin_energy_consumption_index"
    BITCOIN_ABBREVIATION = "bitcoin_abbreviation_Abbrev"
    CRYPTO_TWEETS = "crypto_tweets_created_at"
    BTC_TWEETS_SENTIMENTS = "btc_tweets_sentiments_index"
    ETH_TWEETS_SENTIMENTS = "eth_tweets_sentiments_index"
    DOGE_TWEETS_SENTIMENTS = "doge_tweets_sentiments_index"
    
class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"
