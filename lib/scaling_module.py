# Copyright (C) 2020-2021 Elisa Zuccolo, Eucentre Foundation
#
# OpenSel is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenSel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenSel. If not, see <http://www.gnu.org/licenses/>.

def scaling_module(site_code, probability_of_exceedance_num,
                   intensity_measures, output_folder, n_gm,
                   path_nga_folder, path_esm_folder):
    import numpy as np
    import pandas as pd
    from lib.scale_acc import scale_acc

    for ii in np.arange(len(site_code)):
        site = site_code[ii]
        for jj in np.arange(len(probability_of_exceedance_num)):
            poe = probability_of_exceedance_num[jj]
            for im in np.arange(len(intensity_measures)):
                name = intensity_measures[im] + '-site_' + str(
                    site) + '-poe-' + str(poe)

                name_summary = (output_folder + '/' + name + '/' + name +
                                "_summary_selection.txt")

                summary = pd.read_csv(name_summary, sep=' ', skiprows=3)
                scale_acc(n_gm, summary.recID_NGA, path_nga_folder,
                          path_esm_folder, summary.source,
                          summary.event_id_esm, summary.station_code_esm, name,
                          output_folder, summary.scale_factor)
    return
