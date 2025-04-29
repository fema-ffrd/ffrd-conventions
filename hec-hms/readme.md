# HEC-HMS Naming Conventions
    Naming Convention Schema for HEC-HMS model files, names, elements

    schema version: 0.2.0

    Description: This schema defines the naming conventions for various elements in the flood risk model.


| Property          | Type   | Description            | Pattern                       | Examples                             |
|:------------------|:-------|:-----------------------|:------------------------------|:-------------------------------------|
| project_title     | string | Project name           | ^[a-z0-9-]+(_\d+)?$           | trinity, rock-river_1, rock-river_2  |
| basin_title       | string | Basin file name        | ^[a-z0-9-]+_[a-z0-9-]+$       | big-horn_feb1997, trinity_por        |
| met_title         | string | Met file name          | ^[a-z0-9-]+$                  | apr1997, por, sst                    |
| control_title     | string | Control file name      | ^[a-z0-9-]+$                  | apr1997, por, sst                    |
| run_title         | string | Run file name          | ^[a-z0-9-]+$                  | trinity                              |
| subbasin_element  | string | Subbassin element name | ^[a-z0-9-]+_s\d{3}$           | white-rock-ck_s040                   |
| reach_element     | string | Reach element name     | ^[a-z0-9-]+_r\d{3}$           | trinity-river_r070                   |
| junction_element  | string | Junction element name  | ^[a-z0-9+-]+_j\d{3}$          | west-fork_j090, nid_tx05966+out_j010 |
| reservoir_element | string | Reservoir element name | ^nid_[a-z]{2}\d{5}(_s\d{3})?$ | nid_tx05966, nid_mn00584_s002        |
| diversion_element | string | Diversion element name | ^[a-z0-9-]+_d\d{3}$           | lost-creek-diversion_d001            |
| sink_element      | string | Sink element name      | ^[a-z0-9-]+$                  | trinity-bay                          |
| source_element    | string | Source element name    | ^source_[a-z0-9-]+$           | source_trinity-bay                   |
