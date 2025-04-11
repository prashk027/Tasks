'''Examples of MutliProcessing'''
import concurrent.futures
import time
import multiprocessing

start = time.perf_counter()
def do_something(seconds):
    print(f"Sleeping {seconds} second....")
    time.sleep(seconds)
    # print("Done Sleeping")
    return f"Done Sleeping..... {seconds}"

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    '''Previous code for processpoolexecutor'''
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5,4,3,2,1]
    #     results = [executor.submit(do_something,sec) for sec in secs]

    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())

    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something,args=[1])
    #     p.start()
    #     processes.append(p)
    
    # for process in processes:
    #     process.join()

    end = time.perf_counter()

    print(f"Finished in {round(end-start,2)} seconds(s)")




'''How to use Process in code'''
# from multiprocessing import Process


# def print_func(continent='Asia'):
#     print('The name of continent is : ', continent)

# if __name__ == "__main__":  # confirms that the code is under main function
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()

#     # instantiating process with arguments
#     for name in names:
#         # print(name)
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()

#     # complete the processes
#     for proc in procs:
#         proc.join()

'''Download Images from picsum using multiprocessing'''
# import multiprocessing
# import requests

# print("No. of CPU: ",multiprocessing.cpu_count())

# def downloadFile(url,name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg","wb").write(response.content)
#     print(f"Finished Downloading {name}")


# if __name__ == "__main__":
#     url = "https://picsum.photos/2000/3000"
#     pros = []

#     for i in range(50):
#         p = multiprocessing.Process(target=downloadFile, args=[url,i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()
