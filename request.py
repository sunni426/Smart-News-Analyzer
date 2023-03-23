'''
    The GIL is a single lock on the interpreter itself which adds a rule that 
    execution of any Python bytecode requires acquiring the interpreter lock

    implement analyzer 

    queue class in each 

    kwargs

    request job, keep track of job id, and keep track of thread id

    - implement request class: general class to take in requests (wih func and func arg)
    as arguments, create a thread (& keep up with thread id), which will run the actual func
    such as upload pdf. when it finishes, calls callback func
    - implement running queue (perhaps in a class or as a global variable)
    - callback functions with threads (callback, ex. can decrement threads_active)
    callback as means of communication between main & new threads. will send output etc back

    - in class PDFuploader: init --> create queue. also in classs, and addjob

    - implement logging

    thread1 = requesr()
    thread1.start()


'''