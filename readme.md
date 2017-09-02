# Automatic backup of notes from [Simplenote](https://simplenote.com/) to S3
Script for Amazon Lambda, which backs up all your notes to S3.

Before uploading to Lambda its necessary to install **requests** library by running  `pip install requests -t ./` in repo home, fill out your Simplenote e-mail, bucket name and Simplenote token in `credentials.py`.

![How to get token](https://cmrdyg-db3pap001.files.1drv.com/y4mWPOZhGR_ZghlAAfYOyoQUOSnWuE7D_qN97cBLg7YAmBgXvl3MOKDKHSu-uKsG4D-1FNLe39cjFdLeTOPbHZ_2422NOxL1XnEs1eG64VmE-jIyl9yOYq6inW8g1XkJG8KpTNsD1_rvF3wrJYymuXSlfVAA9cxE3Hhxo0bFfVSEdTJznqGN3--Eg6fXah1pwvzojGdOiutQcsQbE9KqAtbMLxUkGm8knl1v2Y5Ekndy10/get_sn_token.png?psid=1)

After all you have to [ZIP whole repo and upload it to Lambda](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html).

Function needs [approval for writing to S3](http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-create-iam-role.html) and [trigger, which runs it](http://docs.aws.amazon.com/lambda/latest/dg/with-scheduled-events.html).