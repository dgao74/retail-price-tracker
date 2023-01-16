# retail-price-tracker

This application is built to periodically track the price of one web retail item on an hourly basis (by default, a Gigabyte RTX 3080 Ti). This can be adjusted in the code by changing the URL and the elements of the page selected to those of a different item from a different site (success varies depending on the site's policies on scrapers).

Limitation: the app is built for use with Gmail, and would need significant changes to work with other email services. This would be accounted for and improved upon in a future build.

All global variables at the top of the script should be changed to suit the user's needs. This includes the item URL, relevant information (email address, user agent, gmail app password), and the price limit, to be decided by the user. By default, it has been set to 1500, an arbitrary number. Note that the email address entered will be both the sender and receiver of the email sent by the script.

To test for functionality, flip the comparison operator in the if statement on line 25 so that it matches the following:

	if(price_int > price_limit):

This will incorrectly send an email that says that the price has indeed dropped below the set price threshold (in reality it has not; you've just told the script to send you the email if the current price is greater than the price threshold, which it likely is). This is useful for testing if the information has been entered correctly and/or if the code has been written correctly (haha). To revert it so it is accurate, simply flip the operator again, so that the line matches the following:

	if(price_int < price_limit):

Have fun tracking!
