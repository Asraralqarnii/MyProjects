using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using RandomPasscode.Models;
using Microsoft.AspNetCore.Http;


namespace RandomPasscode.Controllers
{
    public class HomeController : Controller
    {
       [HttpGet("")]
        public IActionResult Index()
        {
            if (HttpContext.Session.GetInt32("Count") == null)
            {
                HttpContext.Session.SetInt32("Count",1); 
            }
            else
            {
                int count = (int)HttpContext.Session.GetInt32("Count");
                HttpContext.Session.SetInt32("Count",count + 1);
            }
            ViewBag.Count=HttpContext.Session.GetInt32("Count");

            Random rand = new Random();
            string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            string id ="";

            for(int i = 0; i< 14;i++){
                id += chars[rand.Next(0,chars.Length)];
            }
            ViewBag.passcode=id;

            return View("Index");
        }

        // Clear Session
        [HttpGet("reset")]
        public IActionResult Reset()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}
