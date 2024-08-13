# پیشبینی قیمت طلا با مدل هوش مصنوعی و دستیار تریدر 

## در مرحله اول نیاز به دیتا قیمت طلا داریم  
- برای این دیتا نیاز داریم که اطلاعات رو با استفاده از selenium از توی سایت tradingview  دربیاریم

 ![image](https://github.com/user-attachments/assets/57669c31-8919-45cf-9319-1bbc859fa212)
 
  سایت tradingview رو با استفاده از selenium در  فایرفاکس باز میکنیم به url(چارت قیمت طلا ) مد نظرمون به صورت دستی میریم چون معمولا url  ها عوض میشن یا تحت مراقبت هستن (این فایل توی سورس کدم : CreateDataframe/getinformation_mainA.py):
  
![image](https://github.com/user-attachments/assets/ed52ecf3-bbcd-45b6-bd4d-fc249c44a0b5)



  مشکلی که توی tradingview وجود داره اینه که بعد از چند ثانیه از شما میخواد که بگید ربات نیستید و لاگین کنید (در صورتی که ما واقعا ربات هستیم :) ) 
  پس قبل از اینکه عملیات رو شروع کنیم بهتره که عملیات رو متوقف کنیم و زمانی که آماده بودیم و لاگین کردیم به برنامه اعلام کنیم که ادامه کار رو پیش ببره (در غیر این صورت به مشکل بر میخوریم )

  
![image](https://github.com/user-attachments/assets/1ba92878-d352-46ac-b0c2-1f363bcbaee2)



- این دیتا باید حاوی اطلاعات روزانه قیمت طلا از سال 2023 تا 2007 باشه  با جزئیات کامل (high,low,volume,close,open)

  بعد از اینکه y (تایید برای ادامه کار برناممون ) رو بزنیم موس به صورت خودکار روی صفحات تردینگ ویو میچرخه و دیتا مورد نظر رو برمیداره (این اتفاق با کتابخونه pyautogui رخ میده)
  هرکدوم از این کندل ها یه روز هستن که حاوای اطلاعات  high low open close volume هستن که توی عکس پایین هایلایتشون کردم
  
  
  ![detail we need ](https://github.com/user-attachments/assets/8cde1696-5bc8-45a4-bd9c-ea899c1594a0)

- دیتا باید به حالت خاصی (قابل درک برای مدل ها )در اکسل با استفاده از کتابخونه Pandas  ذخیره بشه
  ![image](https://github.com/user-attachments/assets/0fe19a47-3c2c-4db5-9da2-82c825411f3b)

  توی این مرحله دیتا ها رو باید بر حسب نیازمون سیو کنیم دقت کنید که باید با استفاده از رجکس بیایم هر ستون رو مختص خودش قرار بدیم

  ![image](https://github.com/user-attachments/assets/6b438607-3c1c-441d-8e15-f17ce92f9e41)

در نهایت چنین دیتایی خواهیم داشت قیمت طلا با جزئیات کامل از سال 2007 تا سپتامبر 2023 

![image](https://github.com/user-attachments/assets/8af71b18-690a-46ed-94ba-4018856c156f)


## در مرحله دوم دیتا تمیز شده (data manipulation with pandas )  رو به مدل هوش مصنوعی خودمون میدیم 
برای دیدن جزئیات کد های این بخش میتونید وارد فایل (gold price lstm) بشید و جزئیات کد هارو ببینید (البته بدانید و آگاه باشید بخشی از این کد ها سایت کگل اومده و من ننوشتمشون (متخصص هوش مصنوعی نیستم چون ))
دیتا کل این سال هایی که در اوردیم توی یه نمودار : 
![image](https://github.com/user-attachments/assets/ca487cdf-aa13-408c-916b-69d516412989)


حالا دیتا هارو ترین میکنیم و میایم از هوش مصنوعی میخوایم که برامون قیمت طلا رو از سال 2022 تا 2023 پیشبینی (خودش میره بر حسب 2007 تا 2022 آموزش میبینه و سال آخر رو حدس میزنه تا میزان دقت خودش رو بتونیم تست کنیم (البته خودش که نه مدلی که آقاعه توی کگل نوشته)) کنه تا ببینیم چند درصد درست پیشبینی میکنه 
همونجور توی عکس پایین میبینید تقریبا خطای آقای هوش مصنوعی میل میکنه به صفر و 98.9 درصد دقت داره 
![image](https://github.com/user-attachments/assets/f90afbb1-0b68-493b-97ac-a0775f4427fe)

عکس پایین شاید باعث شه توضیحات بالارو بهتر درک کنید 
![image](https://github.com/user-attachments/assets/368eb11e-fdf8-49f1-b4bc-f4864edd709d)




## ساخت دستیار تریدر 


