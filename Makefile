package: clean
	zip kreader.zip kreader.py
	zip recordstatus.zip recordstatus.py

deploy:
	aws s3 cp kreader.zip s3://$(DEPLOY_BUCKET)
	aws s3 cp recordstatus.zip s3://$(DEPLOY_BUCKET)

clean:
	rm -f *.zip
