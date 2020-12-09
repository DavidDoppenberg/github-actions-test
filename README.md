# github-actions-test
This a markdown file

Known limitations:
1. When you do a commit, but do not change the image (no change in the docker file or not change in the python code) a reference is made to the old image, because nothing changed. This will result in the workflow to crash, because the remove image step relies on that the new image has a different ID.
2. When there is no docker container to remove the remove and/or kill commandows will throw an error
3. The markdown file is not in the container, but on the VM