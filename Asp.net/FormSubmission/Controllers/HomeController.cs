using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using FormSubmission.Models;

namespace FormSubmission.Controllers
{
    public class HomeController : Controller
    {


        [HttpGet("")]
        public IActionResult Index()
        {
            return View("Index");
        }

        [HttpPost("")]
        public IActionResult Create(User user)
        {
            User newUser = user;
            if (ModelState.IsValid)
            {
                return View("Show",newUser);
            }
            else
            {
                return View("Index");
            }

        }

        
    }
}
