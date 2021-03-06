# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_tests(
  name = 'address',
  sources = ['test_address.py'],
  dependencies = [
    'src/python/pants/base:build_file',
    'src/python/pants/base:build_root',
    'src/python/pants/build_graph',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:dirutil',
    'tests/python/pants_test:test_base',
  ]
)

python_tests(
  name = 'build_configuration',
  sources = ['test_build_configuration.py'],
  dependencies = [
    'src/python/pants/base:build_file',
    'src/python/pants/build_graph',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:dirutil',
  ]
)

python_tests(
  name = 'subproject_integration',
  sources = ['test_subproject_integration.py'],
  dependencies = [
    'tests/python/pants_test:int-test',
  ],
  tags = {'integration'},
)


python_tests(
  name = 'build_file_aliases',
  sources = ['test_build_file_aliases.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'src/python/pants/engine/legacy:graph',
    'tests/python/pants_test/subsystem:subsystem_utils',
  ]
)

python_tests(
  name = 'build_file_parser',
  sources = ['test_build_file_parser.py'],
  dependencies = [
    'src/python/pants/base:build_file',
    'src/python/pants/build_graph',
    'tests/python/pants_test:test_base',
  ]
)

python_tests(
  sources = ['test_build_graph.py'],
  dependencies = [
    'src/python/pants/java/jar',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/build_graph',
    'tests/python/pants_test:test_base'
  ],
)

python_tests(
  name = 'build_graph_integration',
  sources = ['test_build_graph_integration.py'],
  dependencies = [
    'tests/python/pants_test:int-test',
  ],
  tags = {'integration'},
)

python_tests(
  name = 'intermediate_target_integration',
  sources = ['test_intermediate_target_integration.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'tests/python/pants_test:int-test',
  ],
  tags = {'integration'},
)

python_tests(
  name = 'scopes',
  sources = ['test_scopes.py'],
  dependencies = [
    'src/python/pants/base:payload',
    'src/python/pants/base:payload_field',
    'src/python/pants/build_graph',
    'tests/python/pants_test:test_base',
    'tests/python/pants_test/subsystem:subsystem_utils',
  ]
)

python_tests(
  name = 'source_mapper',
  sources = ['test_source_mapper.py'],
  dependencies = [
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/build_graph',
    'tests/python/pants_test:test_base',
  ]
)

python_tests(
  name = 'target',
  sources = ['test_target.py'],
  dependencies = [
    'src/python/pants/base:exceptions',
    'src/python/pants/base:fingerprint_strategy',
    'src/python/pants/base:payload',
    'src/python/pants/build_graph',
    'src/python/pants/source',
    'tests/python/pants_test:test_base',
    'tests/python/pants_test/subsystem:subsystem_utils',
  ]
)

python_tests(
  name = 'files',
  sources = ['test_files.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'src/python/pants/source',
    'tests/python/pants_test:test_base',
  ]
)

python_tests(
  name = 'target_filter_subsystem',
  sources = ['test_target_filter_subsystem.py'],
  dependencies = [
    'src/python/pants/build_graph',
    'src/python/pants/task',
    'tests/python/pants_test:task_test_base',
  ]
)
