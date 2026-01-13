# Add at the top of the file
CACHE_SZ = 1024  # Example cache size in bytes (adjust as needed)
CACHE_LINE_SZ = 64  # 64-byte cache lines
WORDS_PER_LINE = 16  # 16 words per cache line (assuming 4-byte words)

def init_cache():
    """Initialize cache with given size and line size"""
    num_lines = CACHE_SZ // CACHE_LINE_SZ
    cache_storage = [[0] * WORDS_PER_LINE for _ in range(num_lines)]
    location_stack_storage = list(range(num_lines))
    location_stack_ptr = num_lines - 1
    last_used_loc = location_stack_storage[location_stack_ptr]
    location_stack = (location_stack_storage, location_stack_ptr, last_used_loc)
    address_to_cache_loc = {}
    cache_loc_to_address = {}
    cache = (cache_storage, address_to_cache_loc, cache_loc_to_address, location_stack)
    return cache

def get_next_free_location(location_stack):
    """Get next available cache location using stack-based replacement"""
    location_stack_storage, location_stack_ptr, last_used_loc = location_stack
    if location_stack_ptr < 0:
        raise Exception("Cache is full")
    loc = location_stack_storage[location_stack_ptr]
    return (loc, (location_stack_storage, location_stack_ptr - 1, loc))

def evict_location(cache, memory):
    """Evict least recently used cache line back to memory"""
    cache_storage, address_to_cache_loc, cache_loc_to_address, location_stack = cache
    location_stack_storage, location_stack_ptr, last_used_loc = location_stack
    
    if location_stack_ptr >= len(location_stack_storage) - 1:
        raise Exception("No lines to evict")
    
    # Get the line to evict
    evicted_address = cache_loc_to_address[last_used_loc]
    cache_line = cache_storage[last_used_loc]
    
    # Write back to memory
    base_address = evicted_address << 4
    for i in range(WORDS_PER_LINE):
        memory[base_address + i] = cache_line[i]
    
    # Update mappings
    del address_to_cache_loc[evicted_address]
    del cache_loc_to_address[last_used_loc]
    
    # Update stack
    new_stack_ptr = location_stack_ptr + 1
    new_stack_storage = location_stack_storage.copy()
    new_stack_storage[new_stack_ptr] = last_used_loc
    new_stack = (new_stack_storage, new_stack_ptr, last_used_loc)
    
    return ((cache_storage, address_to_cache_loc, cache_loc_to_address, new_stack), memory)

def cache_is_full(location_stack):
    """Check if cache is full"""
    _, location_stack_ptr, _ = location_stack
    return location_stack_ptr < 0

def read_from_mem_on_miss(memory, cache, address):
    """Handle cache miss by reading from memory"""
    cache_storage, address_to_cache_loc, cache_loc_to_address, location_stack = cache
    location_stack_storage, location_stack_ptr, _ = location_stack
    
    # Get free location (assumes space is available)
    loc, new_stack = get_next_free_location(location_stack)
    
    # Read cache line from memory
    base_address = (address >> 4) << 4
    cache_line = [memory[base_address + i] for i in range(WORDS_PER_LINE)]
    
    # Update cache
    cache_storage[loc] = cache_line
    tag = address >> 4
    address_to_cache_loc[tag] = loc
    cache_loc_to_address[loc] = tag
    
    new_cache = (cache_storage, address_to_cache_loc, cache_loc_to_address, new_stack)
    return (memory, new_cache)

def update_cache_entry(cache, address, data):
    """Update existing cache entry"""
    cache_storage, address_to_cache_loc, cache_loc_to_address, location_stack = cache
    tag = address >> 4
    offset = address & 0xF
    
    if tag not in address_to_cache_loc:
        raise Exception("Address not in cache")
        
    loc = address_to_cache_loc[tag]
    cache_storage[loc][offset] = data
    return cache

def fetch_cache_entry(cache, address):
    """Read data from cache"""
    _, address_to_cache_loc, _, _ = cache
    tag = address >> 4
    offset = address & 0xF
    
    if tag not in address_to_cache_loc:
        raise Exception("Address not in cache")
        
    loc = address_to_cache_loc[tag]
    return cache[0][loc][offset]

def write_data_to_cache(memory, cache, address, data):
    """Write data to cache with write-through policy"""
    cache_storage, address_to_cache_loc, _, location_stack = cache
    
    # Check if cache is full and evict if needed
    if cache_is_full(location_stack):
        cache, memory = evict_location(cache, memory)
    
    # Handle cache miss
    tag = address >> 4
    if tag not in address_to_cache_loc:
        memory, cache = read_from_mem_on_miss(memory, cache, address)
    
    # Update cache and memory (write-through)
    cache = update_cache_entry(cache, address, data)
    memory[address] = data
    
    return (memory, cache)

def read_data_from_cache(memory, cache, address):
    """Read data from cache with miss handling"""
    _, address_to_cache_loc, _, location_stack = cache
    
    # Handle cache miss
    tag = address >> 4
    if tag not in address_to_cache_loc:
        if cache_is_full(location_stack):
            cache, memory = evict_location(cache, memory)
        memory, cache = read_from_mem_on_miss(memory, cache, address)
    
    data = fetch_cache_entry(cache, address)
    return (data, memory, cache)