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

@router.get("/isop/{address}", tags=["Read Commands - Related to Operators"])
def isop(address: str):
    """
    Check if address is operator.
    """
    return run_command(["isop", address])

@router.get("/ops", tags=["Read Commands - Related to Operators"])
def ops():
    """
    List all operators.
    """
    return run_command(["ops"])

@router.get("/opnets/{operator_address}", tags=["Read Commands - Related to Operators"])
def opnets(operator_address: str):
    """
    List all networks where operator is opted in.
    """
    return run_command(["opnets", operator_address])

@router.get("/op-vault-net-stake/{operator_address}/{vault_address}/{network_address}", tags=["Read Commands - Related to Operators"])
def op_vault_net_stake(operator_address: str, vault_address: str, network_address: str):
    """
    Get operator stake in vault for network.
    """
    return run_command(["op-vault-net-stake", operator_address, vault_address, network_address])

@router.get("/opstakes/{operator_address}", tags=["Read Commands - Related to Operators"])
def opstakes(operator_address: str):
    """
    Show operator stakes in all networks.
    """
    return run_command(["opstakes", operator_address])

@router.get("/check-opt-in-network/{operator_address}/{network_address}", tags=["Read Commands - Related to Operators"])
def check_opt_in_network(operator_address: str, network_address: str):
    """
    Check if operator is opted in to a network.
    """
    return run_command(["check-opt-in-network", operator_address, network_address])

@router.get("/check-opt-in-vault/{operator_address}/{vault_address}", tags=["Read Commands - Related to Operators"])
def check_opt_in_vault(operator_address: str, vault_address: str):
    """
    Check if operator is opted in to a vault.
    """
    return run_command(["check-opt-in-vault", operator_address, vault_address])

@router.get("/operator-network-limit/{vault_address}/{network_address}/{operator_address}", tags=["Read Commands - Related to Operators"])
def operator_network_limit(vault_address: str, network_address: str, operator_address: str):
    """
    Get a current operator-network limit for an operator in the subnetwork.
    """
    return run_command(["operator-network-limit", vault_address, network_address, operator_address])

@router.get("/operator-network-shares/{vault_address}/{network_address}/{operator_address}", tags=["Read Commands - Related to Operators"])
def operator_network_shares(vault_address: str, network_address: str, operator_address: str):
    """
    Get current operator-network shares for an operator in the subnetwork.
    """
    return run_command(["operator-network-shares", vault_address, network_address, operator_address])

@router.get("/total-operator-network-shares/{vault_address}/{network_address}", tags=["Read Commands - Related to Operators"])
def total_operator_network_shares(vault_address: str, network_address: str):
    """
    Get current total operator-network shares for a subnetwork in a vault.
    """
    return run_command(["total-operator-network-shares", vault_address, network_address])
