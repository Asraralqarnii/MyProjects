using System;

namespace ViewModelFun.Models
{
public class User
{
    public string FirstName { get; set; }
    public string LastName { get; set; }

    public User(string fName = "", string lName = "")
        {
            FirstName = fName;
            LastName = lName;
           
        }

        public string FullName()
        {
            return FirstName + " " + LastName;
        }
}
}