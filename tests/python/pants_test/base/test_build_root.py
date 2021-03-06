# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import unittest

from pants.base.build_root import BuildRoot
from pants.util.contextutil import environment_as, pushd, temporary_dir
from pants.util.dirutil import safe_mkdir, safe_mkdtemp, safe_rmtree, touch


class BuildRootTest(unittest.TestCase):

  def setUp(self):
    self.original_root = BuildRoot().path
    self.new_root = os.path.realpath(safe_mkdtemp())
    BuildRoot().reset()

  def tearDown(self):
    BuildRoot().reset()
    safe_rmtree(self.new_root)

  def test_via_set(self):
    BuildRoot().path = self.new_root
    self.assertEqual(self.new_root, BuildRoot().path)

  def test_reset(self):
    BuildRoot().path = self.new_root
    BuildRoot().reset()
    self.assertEqual(self.original_root, BuildRoot().path)

  def test_via_pants_runner(self):
    with temporary_dir() as root:
      root = os.path.realpath(root)
      touch(os.path.join(root, 'pants'))
      with pushd(root):
        self.assertEqual(root, BuildRoot().path)

      BuildRoot().reset()
      child = os.path.join(root, 'one', 'two')
      safe_mkdir(child)
      with pushd(child):
        self.assertEqual(root, BuildRoot().path)

  def test_temporary(self):
    with BuildRoot().temporary(self.new_root):
      self.assertEqual(self.new_root, BuildRoot().path)
    self.assertEqual(self.original_root, BuildRoot().path)

  def test_singleton(self):
    self.assertEqual(BuildRoot().path, BuildRoot().path)
    BuildRoot().path = self.new_root
    self.assertEqual(BuildRoot().path, BuildRoot().path)

  def test_not_found(self):
    with temporary_dir() as root:
      root = os.path.realpath(root)
      with pushd(root):
        self.assertRaises(BuildRoot.NotFoundError, lambda: BuildRoot().path)

  def test_buildroot_override(self):
    with temporary_dir() as root:
      with environment_as(PANTS_BUILDROOT_OVERRIDE=root):
        self.assertEqual(BuildRoot().path, root)
