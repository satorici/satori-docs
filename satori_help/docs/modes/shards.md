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
  Exclusion file path **or** one direct IP, CIDR or IP range to exclude  
  (e.g., `192.168.1.0/24`, `10.0.0.1-10.0.0.255`). Only IP addresses are excluded: domains and URLs are never filtered out.

- **--results PATH**  
  Output file path (writes to stdout if omitted). Must have a `.txt` extension or no extension (`.txt` is appended by default).


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

- **Direct exclusion**: one CIDR range, one IP range or one single IP. A comma-separated list is not accepted and excludes nothing.

- **Files**: Text files `--exclude file.txt` with IP addresses, CIDR ranges or IP ranges to exclude (one per line). Use a file to exclude more than one range. Lines that start with `#` are ignored.

Exclusions apply to IP addresses only. A domain or URL in `--exclude` has no effect, and domains or URLs in the input are never excluded.


## Usage Examples

### Basic usage with files
```sh
satori-v2 shards --shard 1/10 --input input.txt --exclude exclude.txt --results output.txt
```

### Direct CIDR input
```sh
satori-v2 shards --shard 1/10 --input 0.0.0.0/24 --exclude 192.168.0.0/16 --results output.txt
```

### IP range processing
```sh
satori-v2 shards --shard 1/10 --input 10.0.0.1-10.0.0.255 --exclude 10.0.0.1 --results output.txt
```

## Scan entire IPv4 range in seconds

To divide the entire IPv4 range (4.3 billion addresses) into 500 parts and process only the first slice while excluding private networks:

```sh
printf '10.0.0.0/8\n172.16.0.0/12\n192.168.0.0/16\n' > private.txt
satori-v2 shards --shard 1/500 --input 0.0.0.0/0 --exclude private.txt --results output.txt
```