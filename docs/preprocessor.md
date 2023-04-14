## To run the program:  
``
python preprocessor.py <test_folder>
``

This will read test folder and for each python (.py) file with *filename*: it will

create a folder named: preprocessed_*filename*

within that that folder will be a file for each function seen in the original file
or..
  ``
  
  
  ## Output
  The program removes blank lines and comment lines. It also removes comments after code i.e.
  
  '' 
  if a < b:    # check these two
  ``
  For code before the first function declaration it produces a file *frontmater.py* with comments removed
  If it can determine that there are no functions -- see the test file *testplot.py* then it 
  
  creates a file called *file_main.py* with all the code
  
  ## Limitations
  it will not handle a coment character within quotes correctly -- it doesn't check for quotes
    
  (I will fix this this weekend)
    
  It willnot handle coments with three tics 
  ``
  ''' ...'''
  ``
