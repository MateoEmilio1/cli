from fastapi import APIRouter
import subprocess

router = APIRouter()

def run_command(args: list):
    """
    Ejecuta el comando 'python3 symb.py' con los argumentos dados y retorna el resultado.
    """
    try:
        result = subprocess.run(
            ["python3", "symb.py"] + args,
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
        return {"output": output, "error": error if error else None}
    except Exception as e:
        return {"error": str(e)}

@router.get("/isnet/{address}", tags=["Read Commands - Related to Networks"])
def isnet(address: str):
    """
    Check if address is network.
    """
    return run_command(["isnet", address])

@router.get("/middleware/{network_address}", tags=["Read Commands - Related to Networks"])
def middleware(network_address: str):
    """
    Get network middleware address.
    """
    return run_command(["middleware", network_address])

@router.get("/nets", tags=["Read Commands - Related to Networks"])
def nets():
    """
    List all networks.
    """
    return run_command(["nets"])

@router.get("/netops/{network_address}", tags=["Read Commands - Related to Networks"])
def netops(network_address: str):
    """
    List all operators opted in network.
    """
    return run_command(["netops", network_address])

@router.get("/netstakes/{network_address}", tags=["Read Commands - Related to Networks"])
def netstakes(network_address: str):
    """
    Show stakes of all operators in network.
    """
    return run_command(["netstakes", network_address])

@router.get("/max-network-limit/{vault_address}/{network_address}", tags=["Read Commands - Related to Networks"])
def max_network_limit(vault_address: str, network_address: str):
    """
    Get a current maximum network limit for a subnetwork in a vault.
    """
    return run_command(["max-network-limit", vault_address, network_address])

@router.get("/network-limit/{vault_address}/{network_address}", tags=["Read Commands - Related to Networks"])
def network_limit(vault_address: str, network_address: str):
    """
    Get a current network limit for a subnetwork in a vault.
    """
    return run_command(["network-limit", vault_address, network_address])

@router.get("/pending-resolver/{vault_address}/{network_address}", tags=["Read Commands - Related to Networks"])
def pending_resolver(vault_address: str, network_address: str):
    """
    Get a pending resolver for a subnetwork in a vault.
    """
    return run_command(["pending-resolver", vault_address, network_address])

@router.get("/resolver/{vault_address}/{network_address}", tags=["Read Commands - Related to Networks"])
def resolver(vault_address: str, network_address: str):
    """
    Get a current resolver for a subnetwork in a vault.
    """
    return run_command(["resolver", vault_address, network_address])
