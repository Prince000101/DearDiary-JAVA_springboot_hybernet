export const useRegister = () => {
    const [data, setData] = useState<RegisterData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const controller = new AbortController();
        fetchRegister(controller.signal)
            .then(setData)
            .catch(err => setError(err.message))
            .finally(() => setLoading(false));
        return () => controller.abort();
    }, []);

    return { data, loading, error, refetch: () => fetchRegister() };
};


export function validateDashboard(data: DashboardInput): ValidationResult {
    const errors: Record<string, string> = {};

    if (!data.email || !isValidEmail(data.email)) {
        errors.email = 'A valid email is required';
    }
    if (!data.password || data.password.length < 8) {
        errors.password = 'Password must be at least 8 characters';
    }

    return {
        valid: Object.keys(errors).length === 0,
        errors,
    };
}
