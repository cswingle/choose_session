Choose Session
==============

Very simple python script that reads a CSV of conference or workshop session
times and titles, and a CSV of the titles you wish to attend and displays a
list of the best choices based on your rankings of the sessions.

Files:

* ``find_sessions.py``: the python script.

* ``sessions_with_score.csv``: an example CSV showing the input format.

Usage
-----

* Create a CSV file (with a header row) that contains three columns:

  * Date / time of each session block

  * The name of an individual session

  * How interested you are in the session.  This should be a number; larger
    numbers indicate more interest.

* Run it:

.. code:: bash

    $ ./find_sessions.py sessions_with_score.csv

Example
-------

Here's one result from the example file::

   2016-06-14T11:30:00Z:  Debugging and profiling
   2016-06-14T14:00:00Z:  EE 101B
   2016-06-15T10:00:00Z:  Exporting, importing, and rendering
   2016-06-15T12:00:00Z:  Time series analysis
   2016-06-15T14:30:00Z:  Cloud removal
   2016-06-15T16:30:00Z:  Arrays and matrices
   2016-06-16T09:30:00Z:  Machine learning
   2016-06-16T11:30:00Z:  EE, Python
   ['EE 101A', 'My First Maps', 'Fusion Tables', 'Open Data Kit 1',
   'SkySat', 'Easy interfaces', 'Health applications', 'Web applications',
   'Open Data Kit 2', 'Tour of EE API', 'Forest applications', 'EE and
   Google Cloud Platform', 'Storytelling', 'Water cycle analysis', 'Science
   in the classroom', 'Advanced algorithms', 'Teaching with EE']

Each line shows the date / time and what session was randomly chosen
based on your preferences.  The last lines show which sessions in your
input file were not included.

Bugs
----

You’ll notice in the above example that the script chose “EE 101B” for me, but
didn’t select “EE 101A,” which is a prerequisite for 101B.  The script doesn’t
have any concept of order or dependencies so you’ll have to filter those out
yourself.

.. vim:ft=rst:fenc=utf-8:tw=72:ts=3:sw=3:sts=3:nonumber
