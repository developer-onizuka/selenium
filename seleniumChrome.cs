using System;
using System.IO;
using System.Reflection;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTest
{
    class MainClass
    {
        public static void TakeScreenshot(IWebDriver driver, string saveFile)
        {
            ITakesScreenshot ssdriver = driver as ITakesScreenshot;
            Screenshot screenshot = ssdriver.GetScreenshot();
            screenshot.SaveAsFile(saveFile, ScreenshotImageFormat.Png);
        }

        public static void Main()
        {
            ChromeOptions options = new ChromeOptions();
	    options.AddArgument("--headless");
	    options.AddArgument("--no-sandbox");

	    //Find directory with Chrome Driver
            //Console.WriteLine(Assembly.GetExecutingAssembly().Location);
	    
	    IWebDriver browser = new ChromeDriver(".", options);
            browser.Navigate().GoToUrl(@"https://github.com/developer-onizuka");
	    TakeScreenshot(browser, "./test.png");

            browser.Quit();
        }
    }
}
