from urllib import request
#  Download csv below
goog_url = "http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)  # connect!
    csv = response.read()
    str_csv = str(csv)  # save it as a string
    lines = str_csv.split("\\n")   # takes large string and breaks it up line by line
    destination = r'goog.csv'   # r stands for raw string (for raw file) // make a file on our cpu
    fx = open(destination,"w")

    for line in lines:
        fx.write(line + "\n")  # write to the file

    fx.close()

download_stock_data(goog_url)

