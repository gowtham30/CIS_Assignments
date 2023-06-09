import datetime
from dateutil.relativedelta import relativedelta


def qtfunc(date, quarter):
    #PreviousMonth
    format = '%Y%m'
    date = datetime.datetime.strptime(date, format).date()
    PreviousMonth = date - datetime.timedelta(days=1)
    print("PreviousMonth : ", PreviousMonth.strftime('%Y%m'))
    
    #previous_quarter
    if quarter=="q1":
        previous_quarter= "q4"+"_"+str(date.year - 1)
        
    else:
        quarter_number=int(quarter[1:])
        #print(type(quarter_number))
        previous_quarter ="q"+str(quarter_number-1)+"_"+str(date.year)
    print(previous_quarter)
    FutureMonth = str(date.year + 1)+str(PreviousMonth.month)
    print(FutureMonth)
    
    QUARDO = quarter+"_"+str(date.year)

    print


    
if __name__ == '__main__':
    date = '201805'
    quarter = 'q2'
    qtfunc(date, quarter)