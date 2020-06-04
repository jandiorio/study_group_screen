# DevNet Study Group Skills Check - BASIC

The objective of this basic challenge will help us verify your interest in the study group.  The challenges is designed to be very simple but require some basic python skills for accessing data, reading and writing files.  You can use any resources available to figure out how to get the requirements met.

## Target Outcome
- a python script that creates a YAML file
- the YAML file contains basic information about you
- push only the python file

## Tasks

> NOTE: The branch name and file name should be all lowercase and match the names in your dataset created.

1. Clone a repo

```
git clone https://github.com/jandiorio/study_group_screen
```

2. Create a git branch named `<first_name>_<last_name>`

    - example:  `git checkout -b jeff_andiorio`

3. Create a simple python script named `<first_name>_<last_name>.py` example: `jeff_andiorio.py`
    - Creates a **list** of dictionaries with a **single** dictionary
    - dictionary will have the following keys:  `['first_name', 'last_name', 'company', 'email', 'github_username']`
    - dictionary will have your information as the values
    - convert the list to a YAML string
    - write the YAML string to a file

Your file should look like the example below (key order may vary):

```yaml
- company: WWT
  email: jeff.andiorio@wwt.com
  first_name: Jeff
  github_username: jandiorio
  last_name: Andiorio
```

> TIP: Validation will check the YAML filename components match your data for first_name, last_name and that the YAML data is a single element list with a dictionary of key/value pairs.

4. Add/Commit/Push
    - Add python file - `git add *.py`
    - Commit your changes -  `git commit -m "adds my python script"`
    - Push changes to upstream repository `git push --set-upstream origin jeff_andiorio`

> NOTE: These can all be in the same script.