import os

#Each website you crawl is separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project '+ directory)
        os.makedirs(directory)


#Create queue and crawled files(if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')



#create new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)



#add data or link into an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')



#delete the content of a file
def delete_file_contents(path):
    open(path, 'w').close()



# Read a file and convert each line to set or make a list items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results



# Iterate through a set, each item or link will be a new line in the file tht means save link in the file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
