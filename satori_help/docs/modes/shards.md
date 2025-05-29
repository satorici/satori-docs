# Shards

Satori's shards command allows you to deterministically divide massive input datasets (IPs, domains, or URLs) into smaller chunks for distributed processing.
It supports IPv4 address ranges, domains, and HTTP/S URLs, and offers high-performance filtering using multiprocessing and vectorized exclusion logic.


## Parameters

- **--shard X/Y** *(required)*  
  Shard index `X` out of `Y` total shards.

- **--input PATH** *(required)*  
  Input file path **or** direct IP/CIDR/range/domain/URL  
  (e.g., `192.168.1.0/24`, `10.0.0.1-10.0.0.255`, `example.com`, `https://example.com`).

- **--seed N** *(optional, default: **1**)*  
  Seed for deterministic pseudorandom distribution.

- **--exclude PATH or ENTRY**  
  Exclusion file path **or** direct IP/CIDR/range/domain/URL to exclude  
  (e.g., `192.168.1.0/24`, `10.0.0.1-10.0.0.255`, `example.com`, `https://example.com`).

- **--results PATH**  
  Output file path (writes to stdout if omitted).


## Input Methods

The shards command accepts input in two ways:

### Direct input
- **CIDR notation**: `192.168.1.0/24`, `0.0.0.0/0`
- **IP ranges**: `192.168.1.1-192.168.1.255`
- **Single IP**: `192.168.1.1`
- **Domains/URLs**: `example.com`, `https://example.com`

### File-based input
- Text files `--input file.txt` containing IP addresses, CIDR ranges, domains, or URLs (one per line)


## Exclusion Methods

The `--exclude` flag also supports both file-based and direct input:

- **Direct exclusion**: CIDR ranges, IP ranges, single IPs, domains, URLs.

- **Files**: Text files `--exclude file.txt` with IP addresses, CIDR or IP ranges, domains, or URLs to exclude (one per line).


## Usage Examples

### Basic usage with files
```sh
satori shards --shard 1/10 --input input.txt --exclude exclude.txt --results output.txt
```

### Direct CIDR input
```sh
satori shards --shard 1/10 --input 0.0.0.0/24 --exclude 192.168.0.0/16 --results output.txt
```

### IP range processing
```sh
satori shards --shard 1/10 --input 10.0.0.1-10.0.0.255 --exclude 10.0.0.1 --results output.txt
```

## Scan entire IPv4 range in seconds

To divide the entire IPv4 range (4.3 billion addresses) into 500 parts and process only the first slice while excluding private networks:

```sh
satori shards --shard 1/500 --input 0.0.0.0/0 --exclude 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 --results output.txt
```