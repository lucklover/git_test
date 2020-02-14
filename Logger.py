#日志记录程序
#将其他程序的调试输出, 作为日志文件. 输出到本地log文件中去.
#如果存在本地文件夹或者文件夹则在其文件后部直接写入. 如果不存在则创建一个新文件夹和文件.
#log文件命名规则以程序名称+日期为基础.
def logger(error_bad):
    
 try:
    with open('D:/projects/git_test/log/filelog.log','a') as log_file1:
        log_file1.write('\n'+str(error_bad))
        log_file1.close
 except IOError as FER:
    with open('D:/projects/git_test/log/filelog.log','w') as log_file2:
        log_file2.write(str(FER)+'\n'+str(error_bad))
        log_file2.close
        
