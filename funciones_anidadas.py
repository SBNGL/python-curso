def first(datos):
    print(datos)
    
    def second():
        for n in datos:
            print(n)
            
        def third():
            print('HI GUYS')
            
        third()    
            
    second()        
            
first([3, 5, 7, 9])            