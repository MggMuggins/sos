
def dqlite_base_collection(
    plugin,
    pkg: str,
    db_path: str,
    crt_dir: str,
):
    """Conduct a baseline collection that is common for all dqlite-based
    applications, and share common sql queries amongst the relevant
    applications"""

    cert = f"{crt_dir}/cluster.crt"

    # Check for inconsistent dqlite db intervals
    plugin.add_dir_listing(
        db_path,
        suggest_filename=f"ls_{pkg}_dqlite_dir",
    )

    # All dqlite consumers except lxd have info.yaml and cluster.yaml
    plugin.add_copy_spec(
        [
            f"{db_path}/info.yaml",
            f"{db_path}/cluster.yaml",
            f"{db_path}/../daemon.yaml",  # Not expected for microk8s
        ]
    )

    plugin.add_cmd_output(
        f"openssl x509 -in {cert} -noout -dates",
    )
