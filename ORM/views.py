from django.db import connection
from django.shortcuts import render
from .models import Student_Data
from django.http import HttpResponse
from django.db.models import Q


def stu_data(request):

# method return raw sql query
    data = Student_Data.objects.all()

    data1 = Student_Data.objects.filter(stu_marks=78)

    data1 = Student_Data.objects.exclude(stu_marks=78)
    data1 = Student_Data.objects.order_by('stu_name')
    data1 = Student_Data.objects.order_by('-stu_marks')
    data1 = Student_Data.objects.order_by('?')
    data1 = Student_Data.objects.order_by('id').reverse()[0:5]
    data1 = Student_Data.objects.values('stu_name','stu_marks')
    data1 = Student_Data.objects.values('stu_name','stu_marks')
    data1 = Student_Data.objects.using(alias='default')
    


    ############### And or opetator ###########################
    data1 = Student_Data.objects.filter(id=5) & Student_Data.objects.filter(stu_name="devendra")
    data1 = Student_Data.objects.filter(id=51) | Student_Data.objects.filter(stu_name="devendra")
    data1 = Student_Data.objects.filter(id=1,stu_name="devendra") 
    data1 = Student_Data.objects.filter(Q(id=1) & Q(stu_name="devendra")) 
    data1 = Student_Data.objects.filter(Q(id=12) | Q(stu_name="devendra")) 



##################################################################
    # method does not return raw sql query
    data1 = Student_Data.objects.get(id=1) 
    data1 = Student_Data.objects.first() 
    data1 = Student_Data.objects.order_by('stu_name').first() 
    data1 = Student_Data.objects.order_by('stu_name').last() 
    data1 = Student_Data.objects.last() 
    data1 = Student_Data.objects.latest('stu_addmisson_date') 
    data1 = Student_Data.objects.earliest('stu_addmisson_date')
    data1 = Student_Data.objects.create(stu_name='bhai',
        stu_age=20,
        stu_dob='2002-01-01',
        stu_mob='1234567890',
        stu_subject='Math',
        stu_marks=95,
        stu_rank=1,
        stu_collage='Sample College',
        stu_addmisson_date='2023-11-20')
    
    # data1 ,created = Student_Data.objects.get_or_create(stu_name='bhai2',
    #     stu_age=20,
    #     stu_dob='2002-01-01',
    #     stu_mob='1234567890',
    #     stu_subject='Math',
    #     stu_marks=95,
    #     stu_rank=1,
    #     stu_collage='Sample College',
    #     stu_addmisson_date='2023-11-20')
    
    # data1 ,created = Student_Data.objects.update_or_create(stu_name='bhai4',
    #     stu_age=20,
    #     stu_dob='2002-01-01',
    #     stu_mob='1234567890',
    #     stu_subject='Math111',
    #     stu_marks=95,
    #     stu_rank=1,
    #     stu_collage='Sample College',
    #     stu_addmisson_date='2023-11-20',defaults={'stu_name':'bhai4'})
    # print(created)
    
    # data1 = Student_Data.objects.filter(id=5).update(stu_marks="0")
    # data1 = Student_Data.objects.get(id=5)


    dum = [
        Student_Data(stu_name='Jivan ',stu_age=2020-2-1,stu_dob="2222-2-2",stu_mob=89879879,stu_marks=45,stu_rank=88,stu_addmisson_date="2122-3-4"),
        Student_Data(stu_name='ok bhai ',stu_age=2020-2-2,stu_dob="2222-2-2",stu_mob=89879879,stu_marks=45,stu_rank=88,stu_addmisson_date="2122-3-4"),
        Student_Data(stu_name='mota',stu_age=2020-2-3,stu_dob="2222-2-2",stu_mob=89879879,stu_marks=45,stu_rank=88,stu_addmisson_date="2122-3-4"),
        # Add more instances as needed
    ]
    data1=Student_Data.objects.bulk_create(dum)

    all=Student_Data.objects.all()
    for i in all:
        i.stu_collage="kuch bhi yar"
    data1=Student_Data.objects.bulk_update(all,['stu_collage'])

    data1=Student_Data.objects.filter(stu_subject="").delete()
    # data1=Student_Data.objects.filer(stu_city="kuch bhi yar").delete()
    # data1=Student_Data.objects.all().delete()

    print("-----------------------------------------------------------------------")
    # data1=Student_Data.objects.get(id=1)
    data = Student_Data.objects.all()
    print("RAW QUERY:",data1)
    # Get headers from the first item in the queryset
    header = list(data.values().first())
    # Get rows from the queryset
    rows = list(data.values())



    context = {'headers': header, 'rows': rows,'data1':data1,'data1':data}
    return render(request, 'home.html', context)
