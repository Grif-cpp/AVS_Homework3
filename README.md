# AVS_Homework3
Доброго времени суток, моя домашка по АВС (Иванов Григорий БПИ201)                                                    
Cобирал проект так:                                               
Команды для консоли Windows:                                                
pyinstaller main.py Container.py Films\Cartoon.py Films\Documental.py Films\Film.py Films\Gaming.py  

файловый ввод  .\dist\main\main -f tests\test01.txt answers\answ01.txt                                                                 
случайный ввод  .\dist\main\main -n 1000 answers\answ01.txt                                                                 

Описание ввода в файле Description

Среднее время выполнения программы на тестах:                                                           
количество фильмов-----------время(в секундах)                                        
10------------------------------------0.006                
100-----------------------------------0.008                        
500-----------------------------------0.047                                                                                    
1000----------------------------------0.180                                                                                                         
10000---------------------------------20.20                                                                                              
На небольших значениях разница в скорости работы между программой на С++ без OOP, с OOP и  программой на Python незначительна, однако начиная с количества фильмов 500, разница начинает быть существенной, и при количестве фильмов 10000 программа на Python работает примерно 20 секунд, в то время, как C++ справляется за долю секунды.
