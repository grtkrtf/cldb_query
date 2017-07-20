import django
from changlabdb.backend import *
import itertools

# See the list of tasks in ../query_results.txt (not on Github)
# Or, import above in a Python shell and run: list(Task.objects.all())
task_oi = input('Task ID to query: ')

print(task_oi + ':')
task = Task.objects.get(task_uid = task_oi)
blocks = Block.objects.filter(task=task)
print(sorted([block.block_uid for block in blocks]))

print('Patients with this task:')
task_patients = set(block.session.patient for block in blocks)
print([patient.patient_uid for patient in task_patients])