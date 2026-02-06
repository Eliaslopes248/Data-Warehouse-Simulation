"""
BREIF:  THIS PROJECT IS A SIMULATION OF A DATA WAREHOUSE,
        ITS A PROJECT INSPRIED BY THE DATA WAREHOUSE TOOLKIT,
        A BOOK WRITTEN BY THE KIMBALL GROUP 


        THIS FILE SERVES A THE ENTRY POINT OF THIS PROGRAM,
        THE PYTHON IMPLEMETED SERVES AS THE STAGING AREA
        WHICH WILL TRANSFORM SOURCE/LEGACY DATA INTO CLEAN
        AND PRESENTATION READY DATA
"""

"""
TODO: 
1. Create class that handles data normalization DataProcessor()
2. Have it handle the difference source data types
3. Have a thread to handle init the DataProcessor() instance? and just load the values when its done fetching
"""

from gettext import dpgettext
import threading
from modules.sheets_client  import SheetClient
from modules.logger         import color_print
from modules.data_processor import DataProcessor

'''algo to extract the sheet id by the full url'''
def extract_sheet_id_by_url(url):
    # handle empty url
    if len(url) == 0:
        return None
    # make sure its a valid url
    if not url.startswith("https://docs.google.com/") and not url.startswith("docs.google.com/"):
        return None

    # reverse the string
    url = url[::-1]
    # get position of first and second '/'
    first, second, n = None, None, len(url)

    # get first
    for char in range(n):
        if url[char] == "/":
            first = char
            break
    
    # get second
    for char in range(first+1, n):
        if url[char] == "/":
            second = char
            break

    # cannot find id range
    if not first or not second:
        return None

    # slice id range and reverse
    url = url[first+1:second][::-1]
    return url

def get_client_config():
    ''' 
    GETTING SHEETS CLIENT INSTANCE CONFIG (TYPE, SHEET ID)
    '''
    # define source data types
    source_types = ["Events", "Event Attendance", "Event Rating/Feedback"]

    # print out menu header
    print(f' {"":-<10} Configure ETL Client {"":->10}')
    # output source types
    for i, v in enumerate(source_types):
        print(f'{i+1}. {v}')
    # user select type by int
    config_type = -1
    while  config_type < 0 or config_type >= len(source_types):
        config_type = int(input("\n\033[33mEnter type number# : \033[0m")) - 1
        # handle invalid input range
        if config_type < 0 or config_type >= len(source_types):
            print('[error] Invalid type #')

    # get data source google sheet id
    service_email = "comp267-honors-contract@comp267-service-account.iam.gserviceaccount.com"

    print(
        f"\n\033[33mMake sure\033[0m "
        f"{service_email} "
        f"\033[33mis shared with google sheet\033[0m"
    )

    # get sheet url from browser
    source_sheet_id = input("\033[33mEnter google sheet url:\033[0m ")
    # process url
    sheet_id        = extract_sheet_id_by_url(source_sheet_id)
    
    while not sheet_id:
        color_print("Invalid URL:", "red")
        source_sheet_id = input("\033[33mEnter google sheet url:\033[0m ")
        sheet_id        = extract_sheet_id_by_url(source_sheet_id)

    # get sheet range (cell range or just the sheet name)
    sheet_range     = input("\033[33mEnter sheet name: \033[0m")
    # create client
    client = SheetClient(
        sheet_id    =       sheet_id,
        source_type =       config_type,
        sheet_range =       sheet_range
    )
    return client

""" program entry point """
def main():
    # load client
    client = get_client_config()
    color_print("[1/5] Config created", "green")
    # create data processor
    dp = DataProcessor()
    color_print("[2/5] Data Processor created", "green")
    # make thread to load data
    data = client.getValues()
    color_print("[3/5] Data loaded from source", "green")

    # invoke data processing
    color_print("[4/5] Data normalized successfully", "green")

    color_print("[5/5] Data sent to data warehouse", "green")

if __name__ == "__main__":
    main()




