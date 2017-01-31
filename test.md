### Run scrapy spiders 

1) Clone GitHub repo to local folder
  
    
    git clone git@github.com:srsanalytics/academy.git crawler
        
    or
    
    git clone https://github.com/srsanalytics/academy.git crawler
    
2) Go to the clone folder
 
    ```bash
    cd crawler
    ```

3) Create Python `virtualenv`, if you do not `virtualenv` run next command for install:
 
    ```bash
    sudo apt-get install virtualenv
    ```
    
    after install virtualenv, run command:
    
    ```bash
    virtualenv -p python3 venv
    ```
 
4) Activate Python environment:

    ```bash
    source venv/bin/activate
    ```

5) Install Scrapy and other dependency from requirements.txt file:

    ```bash
    pip install -r requirements.txt
    ```

6) Configure database credentials, look more details in README file.

7) Run command for check all OK:

    ```bash
    scrapy list
    ```
    if you see it:
     ```bash
     (venv)$ scrapy list
     academy
     (venv)$
      ```
      
     that's mean all OK and you can run scraping.

8) Run scraping process:

    ```bash
    scrapy crawl academy
    ```

9) Afterfinished scraping you will see report about Scrapy work, such as:

    ```bash
    {'downloader/request_bytes': 123216,
     'downloader/request_count': 281,
     'downloader/request_method_count/GET': 281,
     'downloader/response_bytes': 14616123,
     'downloader/response_count': 281,
     'downloader/response_status_count/200': 281,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2017, 1, 31, 18, 2, 29, 451854),
     'item_scraped_count': 249,
     'log_count/INFO': 7,
     'request_depth_max': 5,
     'response_received_count': 281,
     'scheduler/dequeued': 281,
     'scheduler/dequeued/memory': 281,
     'scheduler/enqueued': 281,
     'scheduler/enqueued/memory': 281,
     'start_time': datetime.datetime(2017, 1, 31, 18, 1, 50, 84404)}
    ```
