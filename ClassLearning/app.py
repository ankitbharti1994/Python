def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonLocal():
        nonlocal spam
        spam = 'non local spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print('after local assignment: ', spam)
    do_nonLocal()
    print('after non-local assignment: ', spam)
    do_global()
    print('after global assignment: ', spam)

scope_test()
print('in global scope: ', spam)