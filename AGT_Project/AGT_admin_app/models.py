from django.db import models

# Create your models here.
class Depart(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
    
class LeaveType(models.Model):
    name=models.CharField(max_length=100,null=False)  
    def __str__(self):
        return self.name 
    
class Employee_detail(models.Model):
    image=models.ImageField(upload_to="images",null=True,blank=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.BigIntegerField()
    Emp_Id = models.CharField(primary_key=True,max_length=20)
    Department = models.ForeignKey(Depart,on_delete=models.CASCADE)
    Designation = models.CharField(max_length=50)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    BasicPay = models.DecimalField(max_digits=10, decimal_places=2)
    PAN = models.CharField(max_length=10)
    UAN = models.BigIntegerField()
    BankAccount = models.BigIntegerField()
    Location = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    
class LeaveRequest(models.Model):
    Emp_Id = models.ForeignKey(Employee_detail,on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    def __str__(self):
        return f"{self.Emp_Id} {self.start_date} 'to' {self.end_date}"
    
class Payslip(models.Model):
    Emp_Id = models.ForeignKey(Employee_detail,on_delete=models.CASCADE)
    month = models.CharField(max_length=7)
    payslip_pdf = models.FileField(upload_to='payslips/')

    def __str__(self):
        return f"Payslip for {self.month}"
