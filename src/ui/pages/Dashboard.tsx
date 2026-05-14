export const useDashboard = () => {
    const [data, setData] = useState<DashboardData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const controller = new AbortController();
        fetchDashboard(controller.signal)
            .then(setData)
            .catch(err => setError(err.message))
            .finally(() => setLoading(false));
        return () => controller.abort();
    }, []);

    return { data, loading, error, refetch: () => fetchDashboard() };
};


export async function fetchSerializer(signal?: AbortSignal): Promise<SerializerResponse> {
    const response = await fetch(`/api/v1/serializers`, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`,
        },
        signal,
    });

    if (!response.ok) {
        const error = await response.json();
        throw new ApiError(error.message, response.status);
    }

    return response.json();
}
