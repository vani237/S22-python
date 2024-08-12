"""
import jenkins
import csv

jenkins_url='http://3.227.16.75:8000'
jenkins_username='devops'
jenkins_pass='devops'
server = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_pass)


number_jobs=server.jobs_count()
user= server.get_whoami()['fullname']

_jobs=server.get_all_jobs()
job_list=[]
for job in _jobs:
    #print("**********************************************")
    job_list.append([job.get('name'), job.get('url'), job.get('color')])

#print(job_list)  

with open("jenkins_jobs.csv", 'w',newline='') as f:
    writer = csv.writer(f)
    Header=['job_name', 'job_url', 'job_color']
    writer.writerow(Header)
    for j in job_list:
        writer.writerow(j)
"""

#another version
# list jenkins jobs
"""
import jenkins
import csv

def listJenkinJobs(url,username,password):
    server = jenkins.Jenkins(url, username=username, password=password)

    _jobs = server.get_all_jobs()
    job_list=[]
    for job in _jobs:
        job_name= job.get('name')
        job_url= job.get('url')
        job_color=job.get('color')
        job_list.append([job_name,job_url,job_color])
    return job_list
    
def storeJenkinsInfo(file_name,job_list):
    with open(file_name, 'w',newline='') as f:
        writer = csv.writer(f)
        HEADER=['Job_name', 'Job_url', 'Job_color']
        writer.writerow(HEADER)
        for j in job_list:
            writer.writerow(j)
            
jobs=listJenkinJobs('http://3.227.16.75:8080','devops','devops') 
storeJenkinsInfo("week22.csv",jobs)
"""
#secon version


import jenkins
import csv

def listJenkinJobs(url,username,password):
    server = jenkins.Jenkins(url, username=username, password=password)

    _jobs = server.get_all_jobs()
    job_list=[]
    for job in _jobs:
        job_name= job.get('name')
        job_url= job.get('url')
        job_color=job.get('color')
        job_list.append([job_name,job_url,job_color])
    return job_list
    
def storeJenkinsInfo(file_name,job_list):
    with open(file_name, 'w',newline='') as f:
        writer = csv.writer(f)
        HEADER=['Job_name', 'Job_url', 'Job_color']
        writer.writerow(HEADER)
        for j in job_list:
            writer.writerow(j)
            
def main():
    jobs=listJenkinJobs('http://3.227.16.75:8080','devops','devops') 
    storeJenkinsInfo("week22.csv",jobs)
    print("File generated successfully")  
    print('file generated successfull')        

if __name__=="___main___":    
    main()   
    