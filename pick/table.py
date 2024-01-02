def greet(fx):
    def mfx():
       print('hello rekha')
       fx()
       print('hii priya')
    return mfx
    @greet
    def hello():
       print('hello saurabh')
    hello()
