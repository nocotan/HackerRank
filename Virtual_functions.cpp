class Person{
   protected:
    string name;
    int age;
   public:
    virtual void getdata() = 0;
    virtual void putdata() = 0;
    
};

class Professor : public Person
{
    int publications;
    static int cur_id;
    int id;
   public:
   Professor(){
   id = cur_id++;
   }
    void getdata(){
        cin>>name>>age>>publications;
    }
    
    void putdata(){
    cout<<name<<" "<<age<<" "<<publications<<" "<<id<<endl;
        
    }
    
};

class Student : public Person
{
    int marks[6];
    int id;
    static int  cur_id;
   public:
   
   Student(){
   id = cur_id++;
   }
    void getdata(){
        int i;
        cin>>name>>age;
        for(i=0;i<6;i++){
        cin>>marks[i];
        }
        
    }
    void putdata(){
        int i;
        int sum = 0;
        for(i=0;i<6;i++){
            
            sum = sum + marks[i];
        
        }
        cout<<name<<" "<<age<<" "<<sum<<" "<<id<<endl;
        
    }
    
};

int Professor::cur_id = 1;

int Student::cur_id = 1;
