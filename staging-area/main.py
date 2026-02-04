"""
THIS PROJECT IS A SIMULATION OF A DATA WAREHOUSE,
ITS A PROJECT INSPRIED BY THE DATA WAREHOUSE TOOLKIT,
A BOOK WRITTEN BY THE KIMBALL GROUP 


THIS FILE SERVES A THE ENTRY POINT OF THIS PROGRAM,
THE PYTHON IMPLEMETED SERVES AS THE STAGING AREA
WHICH WILL TRANSFORM SOURCE/LEGACY DATA INTO CLEAN
AND PRESENTATION READY DATA
"""
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
        config_type = int(input("\nEnter type number# : ")) - 1
        # handle invalid input range
        if config_type < 0 or config_type >= len(source_types):
            print('[error] Invalid type #')

    # get data source google sheet id
    service_email = 'comp267-honors-contract@comp267-service-account.iam.gserviceaccount.com'
    print(f'\nMake sure {service_email} is shared with google sheet')
    source_sheet_id = input("Enter google sheet url: ")
    # process url
    sheet_id = extract_sheet_id_by_url(source_sheet_id)



# TODO: ADD INPUT FOR SHEET RANGE (CAN BE sheet1 or CELL RANGE AS A STRING)
# TODO: IMPLEMENT GOOGLE SHEETS API CLIENT
# TODO: BE ABLE TO PRINT OUT DATA FROM A SHEET
    




if __name__ == "__main__":
    get_client_config()




