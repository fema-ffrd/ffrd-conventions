# HEC-HMS Naming Conventions
Naming convention schema for HEC-HMS model files, names, and elements.

Schema version: 0.3.0

This schema defines the naming conventions for various elements in the flood risk model.

| Property          | Type   | Name               | Pattern                         | Examples                                 |
|:------------------|:-------|:-------------------|:--------------------------------|:-----------------------------------------|
| project_title     | string | Project Title      | `^[a-z0-9-]+(_\d+)?$`           | `trinity`, `rock-river_1`, `rock-river_2`|
| basin_title       | string | Basin File Title   | `^[a-z0-9-]+_[a-z0-9-]+$`       | `big-horn_feb1997`, `trinity_por`        |
| met_title         | string | Met File Title     | `^[a-z0-9-]+$`                  | `apr1997`, `por`, `sst`                  |
| control_title     | string | Control File Title | `^[a-z0-9-]+$`                  | `apr1997`, `por`, `sst`                  |
| run_title         | string | Run File Title     | `^[a-z0-9-]+$`                  | `trinity`                                |
| subbasin_element  | string | Subbasin Element   | `^[a-z0-9-]+_s\d{3}$`           | `white-rock-ck_s040`                     |
| reach_element     | string | Reach Element      | `^[a-z0-9-]+_r\d{3}$`           | `trinity-river_r070`                     |
| junction_element  | string | Junction Element   | `^[a-z0-9+-]+_j\d{3}$`          | `west-fork_j090`, `nid_tx05966+out_j010` |
| reservoir_element | string | Reservoir Element  | `^nid_[a-z]{2}\d{5}(_s\d{3})?$` | `nid_tx05966`, `nid_mn00584_s002`        |
| diversion_element | string | Diversion Element  | `^[a-z0-9-]+_d\d{3}$`           | `lost-creek-diversion_d001`              |
| sink_element      | string | Sink Element       | `^[a-z0-9-]+$`                  | `trinity-bay`                            |
| source_element    | string | Source Element     | `^source_[a-z0-9-]+$`           | `source_trinity-bay`                     |
