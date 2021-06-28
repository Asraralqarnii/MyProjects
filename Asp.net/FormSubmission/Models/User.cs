using System;
using System.ComponentModel.DataAnnotations;
namespace FormSubmission.Models
{
    public class User
    {

        [Required(ErrorMessage = "First Name is required")]
        [MinLength(4)]
        public string FirstName { get; set; }
 
        [Required(ErrorMessage = "Last Name is required")]
        [MinLength(4)]
        public string LastName { get; set; }
 
        [Required(ErrorMessage = "Age should be positive Number")]
        [Range(1,90)]
        public int Age { get; set; }

        [Required(ErrorMessage = "Email is required")]
        [EmailAddress (ErrorMessage = "Email should be valid")]
        public string Email { get; set; }
        
        [Required(ErrorMessage = "Password is required")]
        [MinLength(8)]
        [DataType(DataType.Password)]
        public string Password { get; set; } 

        public User() { }

    }
    
    
    }