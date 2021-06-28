using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using ViewModelFun.Models;

namespace ViewModelFun.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        [HttpGet("")]
        public IActionResult Index()
        {
            Message message = new Message("Lorem ipsum dolor sit amet, nec stet rebum offendit ne, ius te nullam postulant. Mel meliore deserunt ne, mei id nullam impetus, porro iracundia temporibus pro in. Sed an eruditi recusabo euripidis, ad nusquam percipitur eam.");
            return View("Index", message);
        }
        [HttpGet("numbers")]
        public IActionResult Numbers()
        {
            int[] number = new int[]
        {
           1,
           2,
           3,
           10,
           43,
           5 
        };
        return View("Numbers",number);
        }

        [HttpGet("users")]
        public IActionResult Names()
    {

        User user1 = new User("Asrar", "Alqarni");
        User user2 = new User("Billy", "Jack");
        User user3 = new User("Moose", "Pillips");
        User user4 = new User("Rene", "Ricky");
        User user5 = new User("Bar", "barah");


        User[] names = new User[]
        {
           user1,user2,user3,user4,user5
        };

        return View(names);

    }
    [HttpGet("user")]
public IActionResult Name()
    {

        User user = new User("Asrar", "Alqarni");
        

        return View(user);

    }


    }
}
