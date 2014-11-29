# Mallory McConville
# Interacting with Dropbox via the Console

"""
This script provides a simple means of interacting with a dropbox account.

It is possible to upload, download, delete, and view contents of the root
folder.
"""

import dropbox, json, sys


def upload(client):
    print "What to call file on Dropbox: ",
    newFName = raw_input()
    print "Name of file being uploaded: ",
    oldFName = raw_input()

    try:
        # Open the file for uploading
        f = open(oldFName, 'rb')
        response = client.put_file('/'+newFName, f)
        print "uploaded: ", response["path"]

    except IOError:
        print oldFName, "was not found.\n"


def download(client):
    print "What to call downloaded file: ",
    newFName = raw_input()
    print "Name of file on Dropbox: ",
    oldFName = raw_input()   

    try:
        # Open the file for downloading into
        otpt = open(newFName, 'wb')
        with client.get_file(oldFName) as f:
            otpt.write(f.read())

    except dropbox.rest.ErrorResponse:
        print oldFName, "doesn't exist.\n",


def delete(client):
    print "Name of file to delete: ",
    deleteIt = raw_input()

    try:
        # Delete the specified file
        response = client.file_delete('/'+deleteIt)
        print "deleted: ", response["path"]

    except dropbox.rest.ErrorResponse:
        print deleteIt, "doesn't exist.\n",


def output(client):
    # Print the contents of the root folder
    folderContents = client.metadata('/')
    # Convert the dict containing JSON to a string
    json1 = json.dumps(folderContents)
    # Convert the string to JSON
    json2 = json.loads(json1)
    # We want the paths from the contents section
    jsonData = json2["contents"]
    print "Contents of /: "
    # Print all of the paths contained in the root folder
    for item in jsonData:
        print item.get("path")
    


def main():
    # Create a client that's authorized to access account
    client = dropbox.client.DropboxClient('')
    while True:
        print ("\n1 to upload\n2 to download\n3 to delete\n"
               "4 to print root folder contents\n-1 to quit\n")
        theySay = input()

        if theySay is -1:
            sys.exit("Bye!\n")
        elif theySay is 1:
            upload(client)
        elif theySay is 2:
            download(client)
        elif theySay is 3:
            delete(client)
        else:
            output(client)
    

main()
