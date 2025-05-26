class multipleFunctions():
      def Subfields():
          lists =["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
          for subl in lists:
              print(subl)
              
      def oddEven():
          oddeven=int(input("Enter the number:"))
          if ((oddeven%2)==0):
              print("Even Number")
              message="Even Number"
          else:
              print("Odd Number")
              message="Odd Number"
              return message
              
      def Elegible():
          Gender=(input("Your Gender:"))
          Age=int(input("Your Age:"))
          if (Gender=='Male' and Age<21):
              print("NOT ELIGIBLE")
          elif(Gender=='Female' and Age<18):
              print("NOT ELIGIBLE")
          elif(Gender=='Male' and Age>=21):
              print("ELIGIBLE")
          elif(Gender=='Female' and Age>=18):
              print("ELIGIBLE")
          else:    
              print ("NOT A VALID ENTRY")
                
      def BMI():
          bmi=int(input("Enter BM Index:"))
          if(bmi<18.5):
            print ("BMI Underweight")
            message2="BMI Underweight"
          elif(bmi<=24.9):
              print ("BMI Normal range")
              message2="BMI Normal range"
          elif(bmi<=29.9):
              print("BMI Overweight")
              message2="BMI Overweight"
          else:
              print("BMI Obese")
              message2="BMI Obese"
              return message2    

      def percentage():
            sub1=int(input("Subject1="))
            sub2=int(input("Subject2="))
            sub3=int(input("Subject3="))
            sub4=int(input("Subject4="))
            sub5=int(input("Subject5="))
            Total=(sub1 + sub2 + sub3 + sub4 + sub5)
            Persentage=(Total/500)*100
            print("Total  : ",Total)
            print("Percentage :",Persentage)

      def triangle():
            height=int(input("Height  :"))
            breadth=int(input("Breadth:"))
            print("Area formula     :(Height * Breadth)/2")
            area = (height * breadth)/2
            print ("Area of Trianlge :",area)
            height1=int(input("Height1:"))
            height2=int(input("Height2:"))
            breadth=int(input("Breadth:"))
            perimeter= height1 + height2 + breadth
            print("Perimeter formula:Height1+Height2+Breadth")
            print("Perimeter of Triangle:",perimeter)

       
    
    