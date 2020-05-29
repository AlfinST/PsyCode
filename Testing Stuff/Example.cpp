#include <iostream>
#include <string.h>

using namespace std;

class String
{
    char *str;

    public:
        String(const char *s);
        void change(int index,char c){str[index] = c;}
        char *get(){return str;}
};

String::String(const char *s)
{
    int l = strlen(s);
    str = new char[l+1];
    strcpy(str,s);
}

struct Vector2
{
    float x,y;
};

int main()
{
    Vector2 a = {1,2};
    Vector2 b = a;
    Vector2 c;
    b.y = 5;
    c = b;
    c.x = 2;
    cout<<a.x<<a.y<<endl<<b.x<<b.y<<endl<<c.x<<c.y<<endl;
    String s1("geeksQuiz");
    String s2 =s1;
    s1.change(0,'G');
    cout<<s1.get()<<" ";
    cout<<s2.get();
    String s3 = s2;
    cout<<endl<<s2.get();

}