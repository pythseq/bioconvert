# -*- coding: utf-8 -*-
##############################################################################
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
##############################################################################
""" description """
from bioconvert import ConvBase
from bioconvert import requires


__all__ = ["ABI2FASTA"]


class ABI2FASTA(ConvBase):
    """Convert :term:`ABI` file to :term:`FASTQ` file

    Some description.

    """

    _default_method = "biopython"

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input ABI file
        :param str outfile: output FASTA filename

        """
        super(ABI2FASTA, self).__init__(infile, outfile, *args, **kargs)

    @requires(python_library="biopython")
    def _method_biopython(self, *args, **kwargs):
        from Bio import SeqIO
        records = SeqIO.parse(self.infile, "abi")
        SeqIO.write(records, self.outfile, "fasta")


