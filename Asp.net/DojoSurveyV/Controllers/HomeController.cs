using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using DojoSurveyV.Models;

namespace DojoSurveyV.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index()
        {
            return View("Index");
        }
        [HttpPost("")]
        public IActionResult Create(Survey MySurver)
        {
            Survey newSurvey = MySurver;
            if (ModelState.IsValid)
            {
                return View("Result",newSurvey);
            }
            else
            {
                return View("Index");
            }

        }


       
    }
}
